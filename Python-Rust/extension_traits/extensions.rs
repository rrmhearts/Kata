use std::fmt::Display;

trait Greet {
    fn greet(&self) -> String;
    fn name(&self) -> String {
        "Greetings".to_string()
    }
}

impl Greet for str {
    fn greet(&self) -> String {
        // Here self is a string!!
        format!("Hello, {}!", self)
    }
}
impl Greet for &str {
    fn greet(&self) -> String {
        (*self).greet()
    }
}

trait GreetAgain: Greet {
    fn greet_again(&self) -> String;
}

impl<G: Greet + Display> GreetAgain for G {
    // Here self is a generic type that implements Greet!!
    fn greet_again(&self) -> String {
        format!("{}, Hello again, {}!", self.name(), self)
    }
}

fn main() {
    println!("{}", "world".greet());
    println!("{}", "world".greet_again());
}
