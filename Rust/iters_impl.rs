struct Counter {
    count: usize,
}

impl Counter {
    fn new() -> Self {
        Counter { count: 0 }
    }
}

impl Iterator for Counter {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        self.count += 1;
        if self.count < 6 {
            Some(self.count)
        } else {
            None
        }
    }
}

#[test]
fn calling_next_directly() {
    let mut counter = Counter::new();

    assert_eq!(counter.next(), Some(1));
    assert_eq!(counter.next(), Some(2));
    assert_eq!(counter.next(), Some(3));
    assert_eq!(counter.next(), Some(4));
    assert_eq!(counter.next(), Some(5));
    assert_eq!(counter.next(), None);
}

#[test]
fn using_other_iterator_trait_methods() {
    let sum: usize = Counter::new()
        .zip(Counter::new().skip(1)) // (1,2), (2,3), (3,4), (4,5)
        .map(|(a, b)| a * b) // 1*2, 2*3, 3*4, 4*5
        .filter(|x| x % 3 == 0) // 6, 12
        .sum(); // 6 + 12

    assert_eq!(sum, 18);
}

fn main() {
    let mut counter = Counter::new();

    for _ in 0..5 {
        println!("Counter: {:?}", counter.next());
    }

    let sum: usize = Counter::new()
        .zip(Counter::new().skip(1)) // (1,2), (2,3), (3,4), (4,5)
        .map(|(a, b)| a * b) // 1*2, 2*3, 3*4, 4*5
        .filter(|x| x % 3 == 0) // 6, 12
        .sum(); // 6 + 12
    println!("Sum: {}", sum);
}