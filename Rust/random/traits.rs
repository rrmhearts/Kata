// Filename: src/main.rs (or any .rs file you choose to compile and run)

// Define a struct to represent a Book
// Structs are like custom data types that group related data together.
// They are similar to classes in other languages but are data-oriented.
struct Book {
    title: String,
    author: String,
    pages: u32,
}

// Implement methods and associated functions for the Book struct
// The `impl` block defines behavior associated with a type.
impl Book {
    // Associated function (like a static method) to create a new Book instance
    fn new(title: String, author: String, pages: u32) -> Book {
        Book {
            title,
            author,
            pages,
        }
    }

    // Method to display information about the book
    // `&self` indicates that the method borrows the instance immutably.
    fn display_info(&self) {
        println!("Title: {}, Author: {}, Pages: {}", self.title, self.author, self.pages);
    }
}

// Define a trait for summarizable items
// Traits define a set of methods that a type can implement,
// enabling shared behavior and polymorphism.
trait Summarizable {
    fn summary(&self) -> String;
}

// Implement the Summarizable trait for the Book struct
// This allows Book instances to be treated as Summarizable objects.
impl Summarizable for Book {
    fn summary(&self) -> String {
        format!("{} by {}", self.title, self.author)
    }
}

// The main function is the entry point of the program.
fn main() {
    // Create an instance of the Book struct
    // Like a static method, no self parameter
    let my_book = Book::new(
        String::from("The Lord of the Rings"),
        String::from("J.R.R. Tolkien"),
        1178,
    );

    // Call a method on the Book instance
    // my_book is passed to display_info as &self
    my_book.display_info();

    // Call a method defined by the Summarizable trait
    println!("Summary: {}", my_book.summary());

    // You can also define enums for representing choices or states
    // Enums can hold data within their variants.
    enum Shape {
        Circle(f64), // Represents a circle with its radius
        Rectangle(f64, f64), // Represents a rectangle with width and height
    }

    // You can use a `match` statement to handle different enum variants
    // The `match` statement is powerful for pattern matching.
    let my_shape = Shape::Circle(10.0);
    let sec_shape = Shape::Rectangle(10.0, 9.0);

    match my_shape {
        Shape::Circle(radius) => println!("This is a circle with radius: {}", radius),
        Shape::Rectangle(width, height) => println!("This is a rectangle with dimensions: {}x{}", width, height),
    }

    // Rust encourages composition over inheritance for structuring code
    // This allows for greater flexibility and less coupling in design.
    // For instance, instead of inheriting, you can have a struct
    // that contains another struct as a field.
}


// impl User {
    //     fn new(username: String, email: String) -> User {
    //         User {
    //             username,
    //             email,
    //             active: true,
    //         }
    //     }

    //     fn get_full_info(&self) -> String {
    //         format!("Username: {}, Email: {}, Active: {}", self.username, self.email, self.active)
    //     }
    // }

    //     trait Printable {
    //     fn print(&self);
    // }

    // impl Printable for User {
    //     fn print(&self) {
    //         println!("{}", self.get_full_info());
    //     }
    // }