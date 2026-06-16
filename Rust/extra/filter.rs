

fn main() {
    let numbers = vec![1, 2, 3, 4, 5];

    // 1. We use iter() because we want to preserve the original `numbers` vec
    // 2. We use collect() to package the output into a brand new Vec
    let even_numbers: Vec<i32> = numbers
        .iter() // yields &i32
        .filter(|&&x| x % 2 == 0) // designed to take a reference to &i32 which is &&i32
        .cloned()     // converts &i32 references back into owned i32 values
        .collect();   // aggregates the iterator into Vec<i32>

        // if you use |&x| x % 2 == 0, it will still work because Rust has a trait impl for primitive numbers
        // called impl Rem<i32> for i32 { ... } which uses the context and dereferences the value
        // behind the scenes. It will still compile and work as expected. only works for one layer of deref

    println!("The vector still has {} items: {:?}", even_numbers.len(), even_numbers);
}
