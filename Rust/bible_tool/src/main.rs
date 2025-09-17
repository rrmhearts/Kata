use std::fs::File;
use std::io::{self, BufRead, Write};
use regex::Regex;
use lazy_static::lazy_static;
use colored::*;

// Structure to hold a single Bible verse.
#[derive(Debug, Clone)]
struct Verse {
    book: String,
    chapter: u32,
    verse: u32,
    text: String,
}

impl std::fmt::Display for Verse {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{} {}:{} {}",
            self.book.cyan(),
            self.chapter.to_string().cyan(),
            self.verse.to_string().cyan(),
            self.text
        )
    }
}

// Main function to run the application logic.
fn main() {
    println!("Loading Bible...");
    // Load all verses from the file into memory.
    let bible = match load_bible("bible.txt") {
        Ok(verses) => {
            println!("✅ Bible loaded successfully ({} verses).", verses.len());
            verses
        }
        Err(e) => {
            eprintln!("🔥 Error loading bible.txt: {}", e);
            eprintln!("Please ensure 'bible.txt' is in the same directory and has the correct format.");
            return;
        }
    };

    // Main application loop.
    loop {
        print_menu();
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read line");

        match choice.trim() {
            "1" => lookup_verse(&bible),
            "2" => search_bible(&bible),
            "3" => {
                println!("Goodbye! 🙏");
                break;
            }
            _ => println!("{}", "Invalid choice, please try again.".red()),
        }
    }
}

// Displays the main menu options.
fn print_menu() {
    println!("\n--- Bible Tool Menu ---");
    println!("1. Lookup Verse (e.g., Genesis 1:1)");
    println!("2. Search Text");
    println!("3. Exit");
    print!("> ");
    io::stdout().flush().unwrap();
}


// Parses the bible.txt file and returns a Vector of Verse structs.
fn load_bible(filename: &str) -> io::Result<Vec<Verse>> {
    // We use lazy_static to compile the regex only once.
    lazy_static! {
        static ref RE: Regex = Regex::new(r"^(?P<book>.+?)\s(?P<chapter>\d+):(?P<verse>\d+)\t(?P<text>.+)$").unwrap();
    }

    let file = File::open(filename)?;
    let reader = io::BufReader::new(file);
    let mut bible = Vec::new();

    // Skip the first two header lines.
    for line in reader.lines().skip(2) {
        let line = line?;
        if let Some(caps) = RE.captures(&line) {
            let verse = Verse {
                book: caps["book"].to_string(),
                chapter: caps["chapter"].parse().unwrap_or(0),
                verse: caps["verse"].parse().unwrap_or(0),
                text: caps["text"].to_string(),
            };
            bible.push(verse);
        }
    }
    Ok(bible)
}

// Functionality to look up a specific verse.
fn lookup_verse(bible: &[Verse]) {
    print!("Enter reference (e.g., John 3:16): ");
    io::stdout().flush().unwrap();

    let mut reference = String::new();
    io::stdin().read_line(&mut reference).expect("Failed to read line");

    // Simple parsing for the lookup functionality.
    lazy_static! {
        static ref LOOKUP_RE: Regex = Regex::new(r"^(?P<book>.+?)\s(?P<chapter>\d+):(?P<verse>\d+)$").unwrap();
    }

    if let Some(caps) = LOOKUP_RE.captures(reference.trim()) {
        let book = &caps["book"];
        let chapter: u32 = caps["chapter"].parse().unwrap();
        let verse: u32 = caps["verse"].parse().unwrap();

        // Find the verse in our loaded Bible data.
        let found_verse = bible.iter().find(|v| {
            v.book.eq_ignore_ascii_case(book) && v.chapter == chapter && v.verse == verse
        });

        match found_verse {
            Some(v) => println!("\n{}", v),
            None => println!("\n{}", "Verse not found.".red()),
        }
    } else {
        println!("\n{}", "Invalid reference format. Please use 'Book Chapter:Verse'.".red());
    }
}

// Functionality to search for text within the Bible.
fn search_bible(bible: &[Verse]) {
    print!("Enter search query: ");
    io::stdout().flush().unwrap();

    let mut query = String::new();
    io::stdin().read_line(&mut query).expect("Failed to read line");
    let query = query.trim();

    if query.is_empty() {
        println!("\n{}", "Search query cannot be empty.".yellow());
        return;
    }

    println!("\nSearching for '{}'...", query);
    let mut results_found = 0;

    for verse in bible {
         let all_words_found = &query
            .to_lowercase()
            .split_whitespace()
            .all(|word| verse.text.to_lowercase().contains(word));
        // Case-insensitive search
        if *all_words_found {//verse.text.to_lowercase().contains(&query.to_lowercase()) {
            results_found += 1;
            // Create a highlighted version of the text
            let highlighted_text = verse.text.replace(
                query,
                &query.black().on_yellow().to_string()
            );

            // Print the verse with its reference and highlighted text.
            println!(
                "{} {}:{} {}",
                verse.book.cyan(),
                verse.chapter.to_string().cyan(),
                verse.verse.to_string().cyan(),
                highlighted_text
            );
        }
    }

    if results_found == 0 {
        println!("{}", "No results found.".red());
    } else {
        println!("\nFound {} matching verses.", results_found);
    }
}