#include <iostream>
#include <string>

// Define the inner structure
struct Date {
    int day;
    int month;
    int year;
};

// Define the outer structure containing an instance of 'Date'
struct Student {
    std::string name;
    int age;
    Date dob; // Nested struct
};

int main() {
    // 1. Aggregate Initialization (Sequential)
    // Values are assigned in declaration order
    Student s1 = {"John Doe", 20, {15, 5, 2004}};

    // 2. Designated Initializers (C++20 and later)
    // Allows explicit naming of members for clarity
    // Student s2 = {
    //     .name = "Jane Smith",
    //     .age = 21,
    //     .dob = {.day = 10, .month = 12, .year = 2003}
    // };

    // 3. Dot Operator (Manual Assignment)
    // Useful for updating or initializing members one by one
    Student s3;
    s3.name = "Alice Brown";
    s3.age = 22;
    s3.dob.day = 25;
    s3.dob.month = 11;
    s3.dob.year = 2002;

    // 4. Uniform Initialization (Empty/Zero)
    // Sets all members to their default values (e.g., 0 or empty string)
    Student s4 = {};

    // Output a sample
    std::cout << "Student: " << s1.name << "\n"
              << "Date of Birth: " << s1.dob.day << "/" 
              << s1.dob.month << "/" << s1.dob.year << std::endl;

    return 0;
}
