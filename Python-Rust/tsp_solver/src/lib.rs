// #![allow(unsafe_op_in_unsafe_fn)] // if edition = "2024"

use pyo3::prelude::*;
use itertools::Itertools;

/// Brute-force TSP solver: returns the shortest path order and its distance
// internal pure Rust solver (doesn't depend on PyO3)
fn solve_tsp_rust(cities: &[(f64, f64)]) -> (Vec<usize>, f64) {

    let n = cities.len();
    let mut best_order = Vec::new();
    let mut best_dist = f64::INFINITY;

    // Try all permutations starting at 0 (fix first city)
    for perm in (1..n).permutations(n - 1) {
        let mut order = vec![0];
        order.extend(perm);

        let mut dist = 0.0;
        for i in 0..order.len() - 1 {
            let (x1, y1) = cities[order[i]];
            let (x2, y2) = cities[order[i + 1]];
            dist += ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();
        }
        // Return to start
        let (x1, y1) = cities[*order.last().unwrap()];
        let (x2, y2) = cities[0];
        dist += ((x2 - x1).powi(2) + (y2 - y1).powi(2)).sqrt();

        if dist < best_dist {
            best_dist = dist;
            best_order = order.clone();
        }
    }

    (best_order, best_dist)
}

// Python wrapper
#[pyfunction]
fn solve_tsp(cities: Vec<(f64, f64)>) -> PyResult<(Vec<usize>, f64)> {
    Ok(solve_tsp_rust(&cities))
}

/// Python module definition
#[pymodule]
fn tsp_solver(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve_tsp, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn expected_order_and_distance() {
        // Arrange
        let cities = vec![(0.0_f64, 0.0_f64), (1.0_f64, 1.0_f64)];

        // Act — call the function (no `unsafe` needed). It returns a PyResult<(Vec<usize>, f64)>
        let (order, dist) = solve_tsp_rust(&cities);//.expect("solve_tsp failed");

        // Assert order
        assert_eq!(order, vec![0usize, 1usize]);

        // Assert distance with a small epsilon (floats should be compared approximately)
        let expected = 2.0 * (((1.0_f64 - 0.0_f64).powi(2) + (1.0_f64 - 0.0_f64).powi(2)).sqrt());
        let eps = 1e-12;
        assert!(
            (dist - expected).abs() < eps,
            "distance {} not within {} of expected {}",
            dist,
            eps,
            expected
        );
    }
}

