use pyo3::prelude::*;
use itertools::Itertools;

/// Brute-force TSP solver: returns the shortest path order and its distance
#[pyfunction]
fn solve_tsp(cities: Vec<(f64, f64)>) -> PyResult<(Vec<usize>, f64)> {
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

    Ok((best_order, best_dist))
}

/// Python module definition
#[pymodule]
fn tsp_solver(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(solve_tsp, m)?)?;
    Ok(())
}

