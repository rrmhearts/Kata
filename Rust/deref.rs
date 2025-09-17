

use std::ops::Deref;

// A tuple struct
struct MyBox<T>(T);

impl<T> MyBox<T> {
    // x is NOT stored on the heap
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

impl<T> Deref for MyBox<T> {
    // Associated type
    // Generic type for Deref trait
    type Target = T;

    // &self is a reference to the instance of MyBox
    // Return a reference to the value inside MyBox
    // (First item in the tuple struct)
    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

fn main() {
    let x = 5;
    let y = &x;

    // Box is a smart pointer
    // Pointing to a copy of x on the heap
    // let z = Box::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y); // dereference

    let z = Box::new(x);
    assert_eq!(5, *z); // dereference

    // Can now call deref method
    // on MyBox instance using * operator
    let z1 = MyBox::new(x);
    // Will not dereference automatically
    // until we implement Deref trait for MyBox
    // still a reference to value behind the scenes..
    assert_eq!(5, *z1); // dereference

    // Error without Deref trait implemented
    // error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
    //   --> .\deref.rs:29:19
    //    |
    // 29 |     assert_eq!(5, *z1); // dereference
    //    |                   ^^^ can't be dereferenced

    let m = MyBox::new(String::from("Rust"));
    hello(&m);
    // &MyBox<String> -> &String -> &str
    // Auto! Deref coercion!
    // Would have to do this without deref coercion:
    // hello(&(*m)[..]); // without deref coercion
}

fn hello(name: &str) {
    println!("Hello, {}!", name);
}