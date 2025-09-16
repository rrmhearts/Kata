use rand::seq::SliceRandom;
use rand::thread_rng;

/// Compute Euclidean distance between two cities
fn distance(a: (f64, f64), b: (f64, f64)) -> f64 {
    let dx = a.0 - b.0;
    let dy = a.1 - b.1;
    (dx * dx + dy * dy).sqrt()
}

/// Compute the total length of a path
fn path_length(cities: &[(f64, f64)], path: &[usize]) -> f64 {
    let mut total = 0.0;
    for i in 0..path.len() - 1 {
        total += distance(cities[path[i]], cities[path[i + 1]]);
    }
    total
}

/// Nearest Neighbor heuristic to build an initial tour
fn nearest_neighbor(cities: &[(f64, f64)]) -> Vec<usize> {
    let n = cities.len();
    let mut visited = vec![false; n];
    let mut path = Vec::with_capacity(n + 1);

    let mut current = 0; // Start at city 0
    path.push(current);
    visited[current] = true;

    for _ in 1..n {
        let mut nearest = None;
        let mut nearest_dist = f64::INFINITY;

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

    path.push(path[0]); // return to start
    path
}

/// Apply 2-opt optimization to improve a path
fn two_opt(cities: &[(f64, f64)], mut path: Vec<usize>) -> Vec<usize> {
    let n = path.len();
    let mut improved = true;

    while improved {
        improved = false;

        for i in 1..n - 2 {
            for j in i + 1..n - 1 {
                let d1 = distance(cities[path[i - 1]], cities[path[i]])
                       + distance(cities[path[j]], cities[path[j + 1]]);
                let d2 = distance(cities[path[i - 1]], cities[path[j]])
                       + distance(cities[path[i]], cities[path[j + 1]]);

                if d2 < d1 {
                    path[i..=j].reverse();
                    improved = true;
                }
            }
        }
    }
    path
}

/// Heuristic TSP solver: nearest neighbor + 2-opt
pub fn solve_tsp_heuristic(cities: &[(f64, f64)]) -> (Vec<usize>, f64) {
    if cities.is_empty() {
        return (vec![], 0.0);
    }

    // Try multiple randomized starts (optional improvement)
    let mut best_path = nearest_neighbor(cities);
    best_path = two_opt(cities, best_path);
    let mut best_cost = path_length(cities, &best_path);

    let mut rng = thread_rng();
    for _ in 0..10 { // try 10 random starts
        let mut shuffled: Vec<usize> = (0..cities.len()).collect();
        shuffled.shuffle(&mut rng);
        shuffled.push(shuffled[0]);

        let candidate = two_opt(cities, shuffled);
        let cost = path_length(cities, &candidate);
        if cost < best_cost {
            best_cost = cost;
            best_path = candidate;
        }
    }

    (best_path, best_cost)
}


