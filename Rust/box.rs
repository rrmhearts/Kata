
#[derive(Debug)]
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use List::{Cons, Nil};
fn main() {
    // Not very readable code..
    // Need box because the size of List cannot be known at compile time
    let list =  Cons(1, Box::new(Cons(2, Box::new(Cons(3, Box::new(Nil))))));

    println!("List: {:?}", list);

}