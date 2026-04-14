#include <iostream>
#include <unordered_map>
#include <unordered_set>

int main() {
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

    return 0;
}
