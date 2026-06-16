// 1. Define the generic struct with two placeholder types: K and V
struct SimpleMap<K, V> {
    keys: Vec<K>,
    values: Vec<V>,
}

// 2. Implement methods for the generic struct. 
// We must declare <K, V> right after `impl` so Rust knows they are generic parameters.
impl<K, V> SimpleMap<K, V> {
    // A generic constructor
    fn new() -> Self {
        SimpleMap {
            keys: Vec::new(),
            values: Vec::new(),
        }
    }

    // A method that accepts the generic types as arguments
    fn insert(&mut self, key: K, value: V) {
        self.keys.push(key);
        self.values.push(value);
    }

    // A method that returns a reference to the generic Value (&V).
    // We add a "trait bound" (where K: PartialEq) so we are allowed to use `==` on the keys.
    fn get(&self, key: &K) -> Option<&V> 
    where 
        K: PartialEq 
    {
        for (index, existing_key) in self.keys.iter().enumerate() {
            if existing_key == key {
                return self.values.get(index);
            }
        }
        None // Key wasn't found
    }
}

fn main() {
    // --- CASE 1: Relying on Type Inference ---
    // Rust looks at the .insert() calls below and infers that 
    // this map must be a SimpleMap<&str, i32>
    let mut high_scores = SimpleMap::new();
    high_scores.insert("Alice", 950);
    high_scores.insert("Bob", 820);


    // --- CASE 2: Forcing the Type with Turbofish ---
    // If we want to create an empty map and explicitly lock in the types 
    // right away, we use the turbofish syntax:
    let mut currency_symbols = SimpleMap::<String, char>::new();
    
    currency_symbols.insert(String::from("USD"), '$');
    currency_symbols.insert(String::from("EUR"), '€');

    // Look up a value
    if let Some(symbol) = currency_symbols.get(&String::from("EUR")) {
        println!("The symbol for EUR is: {}", symbol);
    }
}