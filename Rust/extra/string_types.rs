

use std::rc::Rc;
use std::sync::Arc;

fn main() {
    // UTF-8 strings are backwards compatible with ASCII
    // string literals are of type &str 
    let s: &str = "Hello, world!";
    let string_types: Vec<&str> = vec![s, "Another string", "Yet another string"];
    
    for item in string_types {
        println!("{}", item);
    }

    // A String is a growable, heap-allocated data structure
    // Create/modify strings at runtime
    // Wrapper around a vector of bytes (Vec<u8>) 
    let my_string = String::from("Hello, Rust!");
    println!("{}", my_string);

    // A byte string literal is of type &[u8; N]
    // stored in binary program
    // Read/analyze string data without changing
    let in_binary: &str = "Hello, bytes!";
    // short for
    let _static_in_binary: &'static str = "Hello, static bytes!";
    println!("{}", in_binary);

    // A view into a String is a &str - string slice
    let my_str: &str = &my_string;
    // it's a slice of the String, the whole string in this case
    println!("{}", my_str);

    // owned, non-growable, healp-allocated string slice
    // Box<str> instead of &str is useful when you need to own the string data
    let boxed_str: Box<str> = my_string.into_boxed_str();
    let boxed_str_new: Box<str> = Box::from("Hello, boxed str!");
    println!("{}, {}", boxed_str, boxed_str_new);

    // 1. No null terminator in Rust
    // 2. All strings are UTF-8
    // 3. Strings are immutable by default

    // If multiple parts of code need to read the same string data,
    // use Rc<String> or Arc<String> for shared ownership
    let some_large_text: &'static str = "This is some large text that is used in multiple places.";
    // multiple parts of program need to reference subsection
    let subsection: Rc<str> = Rc::from(&some_large_text[5..20]);

    let another_reference = Rc::clone(&subsection);
    println!("Subsection: {}, Another reference: {}", subsection, another_reference);

    // thread safe Atomic Reference Counted
    let text_slice = &some_large_text[..];
    let shared_text: Arc<str> = Arc::from(text_slice);

    let mut handles = vec![];
    for _ in 0..5 {
        let thread_safe_shared = Arc::clone(&shared_text);
        let handle = std::thread::spawn(move || {
            println!("Shared text in thread: {}\n", thread_safe_shared);
        });
        handles.push(handle);
    }   
}       

let http_ok: &[u8; 17] = b"HTTP/1.1 200 OK\r\n";
println!("{:?}", http_ok);