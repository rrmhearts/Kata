use std::collections::HashMap;

#[derive(Debug)]
struct Player {
    username: String,
    level: u32,
    is_online: bool,
}

// You MUST derive PartialEq, Eq, and Hash to use a struct as a HashMap KEY
#[derive(PartialEq, Eq, Hash, Debug)]
struct GridPosition {
    x: i32,
    y: i32,
}

fn main() {
    let mut party = HashMap::new();

    // Insert a struct into the map (as a value)
    // Note: The map takes OWNERSHIP of the String and the Player struct
    party.insert(
        String::from("user_99"),
        Player {
            username: String::from("DragonSlayer"),
            level: 42,
            is_online: true,
        },
    );

    // --- ACCESSING THE STRUCT ---
    if let Some(player) = party.get("user_99") {
        // 'player' is a &Player reference. 
        // Rust automatically dereferences it to look at the fields.
        println!("Found {}! Level: {}", player.username, player.level);
    }

    // --- MUTATING THE STRUCT ---
    // Use .get_mut() if you need to change a field inside the struct
    if let Some(player) = party.get_mut("user_99") {
        player.level += 1; // Level up!
        println!("{} leveled up to {}!", player.username, player.level);
    }

    // Use struct as a key 
    let mut map_items = HashMap::new();

    let spawn_point = GridPosition { x: 0, y: 10 };
    
    // Insert data using the struct as the key
    map_items.insert(spawn_point, String::from("Golden Chest"));

    // Access data using a temporary struct with the same values
    let look_up_pos = GridPosition { x: 0, y: 10 };
    
    if let Some(item) = map_items.get(&look_up_pos) {
        println!("At {:?}, you found a: {}", look_up_pos, item);
    }

    // Entry is the best feature
    let mut word_counts = HashMap::new();
    let text = "apple banana apple cherry banana apple";
    
    for word in text.split_whitespace() {
        // 1. Look up the word.
        // 2. If it doesn't exist, insert 0.
        // 3. Return a mutable reference to the value, then increment it by 1.
        let count = word_counts.entry(word).or_insert(0);
        *count += 1; 
    }
    
    println!("{:?}", word_counts); 
    // Output: {"apple": 3, "banana": 2, "cherry": 1}

}