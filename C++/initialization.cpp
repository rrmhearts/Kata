#include <iostream>
#include <string>
#include <vector>

class Example {
public:
    int val;
    // Constructor using Member Initializer List (Best practice for performance)
    Example(int v) : val(v) { 
        std::cout << "Member Initializer used\n"; 
    }
    
    // Default constructor
    Example() : val(0) {}
};

int main() {
    // --- 1. TYPES OF INITIALIZATION ---
    // Occurs at the moment of variable creation

    // Default initialization: Variable may contain garbage (for primitives)
    int defaultInit; 

    // Copy initialization: Uses the equals sign
    int copyInit = 10; 

    // Direct initialization: Uses parentheses
    int directInit(20); 

    // Uniform/List initialization (C++11): Preferred for safety against narrowing
    int listInit{30}; 

    // Value initialization: Resets to zero or default
    int valueInit{}; 

    // these are dumb
    int p = {40}; // Copy initialization with braces (not recommended)
    int q{50};    // Direct list initialization (preferred)
    int r = int{60}; // Copy initialization with explicit type (not recommended)
    int s{int{70}}; // Direct list initialization with explicit type (preferred)


    // --- 2. TYPES OF ASSIGNMENT ---
    // Occurs AFTER a variable is already created

    int x;          // Declaration
    x = 50;         // Simple assignment
    x += 10;        // Compound assignment (same as x = x + 10)

    // --- 3. CLASS MEMBER INITIALIZATION VS ASSIGNMENT ---
    Example obj(100); // Initialization via constructor
    obj.val = 200;    // Assignment to existing member

    Example objbrace{50}; // Uniform initialization for class member

    // Output values
    std::cout << "Copy Init: " << copyInit << "\n";
    std::cout << "Direct Init: " << directInit << "\n";
    std::cout << "List Init: " << listInit << "\n";
    std::cout << "Value Init: " << valueInit << "\n";
    std::cout << "Assigned x: " << x << "\n";

    return 0;
}
