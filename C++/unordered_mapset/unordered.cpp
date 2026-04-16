#include <iostream>
//standard library version
#include <unordered_map>
#include <unordered_set>
//faster version from github
#include "ankerl/unordered_dense.h"

int main() {
    /**** standard containers:
     * The Standard Library (std::unordered_map): Uses Separate Chaining. 
     * It essentially stores elements in a "bucket" of linked lists. 
     * Because of the C++ standard's requirements for reference stability, 
     * each element must be allocated as a separate "node." 
     * This results in many small allocations and poor cache locality.
     * Use std::unordered_map if you absolutely need pointer stability 
     * (i.e., you store a pointer to an element and expect it to remain 
     * valid forever) or if you are writing code where you cannot add 
     * external dependencies.
     */
    // 1. Unordered Set: Keeping track of unique visitors
    std::unordered_set<int> userIDs = {101, 102, 103};
    userIDs.insert(101); // Won't add it again; sets only keep unique values.

    // 2. Unordered Map: Mapping User ID to their Name
    std::unordered_map<int, std::string> userNames;
    userNames[101] = "Alice";
    userNames[102] = "Bob";

    // Quick lookup: Is user 102 in our system?
    if (userNames.find(102) != userNames.end()) {
        std::cout << "Found user: " << userNames[102] << std::endl;
    }
    /**** ankerl::unordered_dense
     * ankerl::unordered_dense: Uses Open Addressing with Robin Hood Hashing. 
     * It stores all keys and values contiguously in a single std::vector. 
     * This "dense" storage is extremely cache-friendly and eliminates 
     * the overhead of individual node allocations. 
     * Use ankerl::unordered_dense for almost everything else. 
     * It is significantly faster for lookups and iteration, 
     * uses less memory, and is much better suited for high-performance 
     * applications like games, simulations, or data processing. 
    */
    // 1. Create a map
    ankerl::unordered_dense::map<std::string, int> ages;

    // 2. Insert elements
    ages["Alice"] = 30;
    ages.emplace("Bob", 25);
    ages.insert({"Charlie", 35});

    // 3. Fast lookup
    if (auto it = ages.find("Alice"); it != ages.end()) {
        std::cout << "Alice is " << it->second << " years old.\n";
    }

    // 4. Fast iteration (values are contiguous in memory!)
    for (auto const& [name, age] : ages) {
        std::cout << name << ": " << age << "\n";
    }

    // set example
    struct PlayerId {
        uint64_t id;
        // bool operator==(PlayerId const& other) const = default;
    };

    // High-quality hash using the library's built-in wyhash
    struct PlayerHash {
        using is_avalanching = void; // Marker for high-quality hash
        auto operator()(PlayerId const& p) const noexcept -> uint64_t {
            return ankerl::unordered_dense::detail::wyhash::hash(p.id);
        }
    };

    ankerl::unordered_dense::set<PlayerId, PlayerHash> active_players;
    active_players.insert({12345});

    return 0;
}
