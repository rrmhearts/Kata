fn main() {
    // This is how Option is defined, but values are auto imported
    enum Option<T> {
        None,
        Some(T),
    }

    let some_number = Option::Some(5);
    let some_char = Option::Some('e');
    let absent_number: Option<i32> = Option::None;

}
