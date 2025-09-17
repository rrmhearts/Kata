
// Encapsulates the concept of iterating over data structures in Rust
// https://doc.rust-lang.org/std/iter/trait.Iterator.html

// How Iterator Trait is defined
pub trait Iterator {
    // Associated type
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}

#[test]
fn iterator_demonstration() {
    let v = vec![1, 2, 3];

    // Immutable iterator
    let mut v_iter = v.iter();

    // Call next method on iterator
    // Returns Option<&i32>
    assert_eq!(v_iter.next(), Some(&1));
    assert_eq!(v_iter.next(), Some(&2));
    assert_eq!(v_iter.next(), Some(&3));
    assert_eq!(v_iter.next(), None);

    let total: i32 = v.iter().sum();
    assert_eq!(total, 6);
}

#[derive(PartialEq, Debug)]
struct Shoe {
    size: u32,
    style: String,
}

fn shoes_in_size(shoes: Vec<Shoe>, shoe_size: u32) -> Vec<Shoe> {
    // into_iter takes ownership of shoes
    // filter takes a closure that returns true for items to keep
    shoes.into_iter().filter(|s| s.size == shoe_size).collect()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn filters_by_size() {
        let shoes = vec![
            Shoe {
                size: 10,
                style: String::from("sneaker"),
            },
            Shoe {
                size: 13,
                style: String::from("sandal"),
            },
            Shoe {
                size: 10,
                style: String::from("boot"),
            },
        ];

        let in_my_size = shoes_in_size(shoes, 10);
        assert_eq!(
            in_my_size,
            vec![
                Shoe {
                    size: 10,
                    style: String::from("sneaker")
                },
                Shoe {
                    size: 10,
                    style: String::from("boot")
                },
            ]
        );
    }
}

fn main() {

    // Consuming iterator
    let v1 = vec![1, 2, 3];
    let v1_iter = v1.into_iter(); // into_iter takes ownership of v1

    for val in v1_iter {
        println!("Got: {}", val);
    }

    // Mutable iterator
    let mut v2 = vec![1, 2, 3];
    {
        let v2_iter_mut = v2.iter_mut(); // iter_mut gives mutable references
        for val in v2_iter_mut {
            *val += 10; // Modify the value through the mutable reference
        }
    }
    println!("Modified v2: {:?}", v2); // Should print [11, 12, 13]

    let v3: Vec<i32> = vec![1, 2, 3];
    let v3_iter = v3.iter().map(|x| x + 1);
    let v3_collected: Vec<i32> = v3_iter.collect();
    assert_eq!(v3_collected, vec![2, 3, 4]);
}