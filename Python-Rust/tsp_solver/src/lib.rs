// #![allow(unsafe_op_in_unsafe_fn)] // if edition = "2024"

use pyo3::prelude::*;
use itertools::Itertools;
use std::f64::INFINITY;

mod heuristic;           // declare the file as a module

use heuristic::solve_tsp_heuristic; // bring the function into scope

/// Solves the Traveling Salesman Problem (TSP) using Held-Karp DP (bitmasking).
/// cities: slice of (x, y) coordinates
/// returns: (best_path as Vec of indices, best_distance)
pub fn solve_tsp_Held_Karp(cities: &[(f64, f64)]) -> (Vec<usize>, f64) {
    let n = cities.len();
    if n == 0 {
        return (vec![], 0.0);
    }

    // Precompute distances
    let mut dist = vec![vec![0.0; n]; n];
    for i in 0..n {
        for j in 0..n {
            let dx = cities[i].0 - cities[j].0;
            let dy = cities[i].1 - cities[j].1;
            dist[i][j] = (dx * dx + dy * dy).sqrt();
        }
    }

    // dp[mask][i] = shortest path to visit set mask, ending at city i
    let size = 1 << n;
    let mut dp = vec![vec![INFINITY; n]; size];
    let mut parent = vec![vec![None; n]; size];

    dp[1][0] = 0.0; // Start at city 0

    for mask in 1..size {
        for u in 0..n {
            if mask & (1 << u) == 0 { continue; }
            let prev_mask = mask ^ (1 << u);
            if prev_mask == 0 { continue; }
            for v in 0..n {
                if prev_mask & (1 << v) == 0 { continue; }
                let new_dist = dp[prev_mask][v] + dist[v][u];
                if new_dist < dp[mask][u] {
                    dp[mask][u] = new_dist;
                    parent[mask][u] = Some(v);
                }
            }
        }
    }

    // Find best cycle returning to 0
    let mut best_cost = INFINITY;
    let mut last = 0;
    for i in 1..n {
        let cost = dp[size - 1][i] + dist[i][0];
        if cost < best_cost {
            best_cost = cost;
            last = i;
        }
    }

    // Reconstruct path
    let mut path = Vec::with_capacity(n + 1);
    let mut mask = size - 1;
    let mut u = last;
    while let Some(p) = parent[mask][u] {
        path.push(u);
        mask ^= 1 << u;
        u = p;
    }
    path.push(0);
    path.reverse();
    path.push(0); // return to start

    (path, best_cost)
}

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
    // Ok(solve_tsp_rust(&cities))
    // Ok(solve_tsp_Held_Karp(&cities))
    Ok(solve_tsp_heuristic(&cities))
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

