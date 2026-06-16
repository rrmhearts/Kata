// Drop Trait
// The Drop trait in Rust provides a 
// way to run some code when a value goes out of scope.
// https://doc.rust-lang.org/std/ops/trait.Drop.html

use std::ops::Drop;

struct CustomSmartPointer {
    data: String,
}

// Cleanup variable when it goes out of scope
impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data: {}", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };

    // c.drop() // Error! Cannot call drop explicitly
    drop(c); // Explicitly call drop function
    // c is no longer valid here
    println!("CustomSmartPointers created.");
    // c and d will be dropped here in reverse order of creation
}