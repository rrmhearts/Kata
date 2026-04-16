#include <iostream>
#include <string>
#include <vector>
#include "nlohmann/json.hpp"

using json = nlohmann::json;

namespace ns {
    // Nested struct
    struct Address {
        std::string street;
        int zip_code;
    };

    // Main struct containing the nested struct
    struct User {
        std::string name;
        int age;
        Address address; // Nested struct
    };

    // Use macros to generate 'inline' to_json and from_json functions.
    // These must be defined in the same namespace as the structs.
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(Address, street, zip_code)
    NLOHMANN_DEFINE_TYPE_NON_INTRUSIVE(User, name, age, address)
}

int main() {
    // 1. Assignment: New struct assigned to a json object
    ns::User user = {"Alice", 30, {"123 Maple St", 45401}};
    
    // This works because the library finds ns::to_json via ADL
    json j = user; 

    // Output the resulting JSON
    std::cout << "Serialized JSON:\n" << j.dump(4) << "\n\n";

    // 2. Deserialization: JSON object back to a struct
    auto user_back = j.get<ns::User>();

    std::cout << "Deserialized User:\n";
    std::cout << "Name: " << user_back.name << "\n";
    std::cout << "Street: " << user_back.address.street << "\n";

    // 3. Deserialization: JSON object back to a struct through assignment
    ns::User user_back2;
    user_back2 = j; // This also works due to ADL finding from_json

    std::cout << "Deserialized User:\n";
    std::cout << "Name: " << user_back2.name << "\n";
    std::cout << "Street: " << user_back2.address.street << "\n";
    return 0;
}