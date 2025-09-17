use rand::seq::SliceRandom;
use rand::thread_rng;
use std::f64::INFINITY;

/// Compute Euclidean distance between two cities
fn distance(a: (f64, f64), b: (f64, f64)) -> f64 {
    let dx = a.0 - b.0;
    let dy = a.1 - b.1;
    (dx * dx + dy * dy).sqrt()
}

/// expects a *closed* path (first == last), sums edges path[i] -> path[i+1]
fn path_length_closed(cities: &[(f64, f64)], path: &[usize]) -> f64 {
    if path.len() < 2 {
        return 0.0;
    }
    let mut total = 0.0;
    for i in 0..path.len() - 1 {
        total += distance(cities[path[i]], cities[path[i + 1]]);
    }
    total
}

fn nearest_neighbor(cities: &[(f64, f64)]) -> Vec<usize> {
    let n = cities.len();
    let mut visited = vec![false; n];
    let mut path = Vec::with_capacity(n + 1);

    let mut current = 0usize;
    path.push(current);
    visited[current] = true;

    for _ in 1..n {
        let mut nearest = None;
        let mut nearest_dist = INFINITY;
        for j in 0..n {
            if !visited[j] {
                let d = distance(cities[current], cities[j]);
                if d < nearest_dist {
                    nearest_dist = d;
                    nearest = Some(j);
                }
            }
        }
        current = nearest.unwrap();
        visited[current] = true;
        path.push(current);
    }

    // make it a closed tour (duplicate start at end)
    path.push(path[0]);
    path
}

/// two_opt expects a closed path (first == last)
fn two_opt(cities: &[(f64, f64)], mut path: Vec<usize>) -> Vec<usize> {
    let n = path.len();
    if n <= 3 {
        return path; // nothing to optimize for < 2 real cities
    }

    let mut improved = true;
    while improved {
        improved = false;
        // iterate through possible i,j pairs (skip the first element at index 0)
        for i in 1..n - 2 {
            for j in i + 1..n - 1 {
                let a = path[i - 1];
                let b = path[i];
                let c = path[j];
                let d = path[j + 1];

                let d1 = distance(cities[a], cities[b]) + distance(cities[c], cities[d]);
                let d2 = distance(cities[a], cities[c]) + distance(cities[b], cities[d]);

                if d2 < d1 {
                    path[i..=j].reverse();
                    improved = true;
                }
            }
        }
    }
    path
}

/// Public heuristic solver.
/// Returns (path_without_final_duplicate, total_cost_including_return_edge)
pub fn solve_tsp_heuristic(cities: &[(f64, f64)]) -> (Vec<usize>, f64) {
    if cities.is_empty() {
        return (vec![], 0.0);
    }

    // Build closed tour and improve it
    let mut path = nearest_neighbor(cities);
    path = two_opt(cities, path);

    // Compute cost using the closed path
    let cost = path_length_closed(cities, &path);

    // Remove the final duplicate start index BEFORE returning so tests expecting [0,1] succeed
    if path.len() >= 2 && path[0] == path[path.len() - 1] {
        path.pop();
    }

    (path, cost)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn expected_order_and_distance_heuristic() {
        // Arrange
        let cities = vec![(0.0_f64, 0.0_f64), (1.0_f64, 1.0_f64)];

        // Act — call the function (no `unsafe` needed). It returns a PyResult<(Vec<usize>, f64)>
        let (order, dist) = solve_tsp_heuristic(&cities);//.expect("solve_tsp failed");

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

