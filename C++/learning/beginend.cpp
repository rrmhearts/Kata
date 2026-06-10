#include <iostream>
#include <string>

template <typename T>
class Container {
private:
    // Storing elements in an array so memory is contiguous.
    // This allows us to use raw memory pointers as iterators.
    T values[2]; 

public:
    Container(T v1, T v2) {
        values[0] = v1;
        values[1] = v2;
    }

    // ITERATOR SETUP:
    // begin() returns a pointer to the very first element.
    T* begin() {
        return &values[0]; 
    }

    // end() returns a pointer to ONE PAST the last element.
    // In C++, the end iterator should never actually be read/dereferenced.
    T* end() {
        return &values[2]; 
    }
};

int main() {
    Container<std::string> words("Iteration", "Achieved!");

    // The C++11 Range-based for loop. 
    // Under the hood, this translates roughly to:
    // for(auto it = words.begin(); it != words.end(); ++it) { auto w = *it; ... }
    for (const std::string& w : words) {
        std::cout << w << " ";
    }
    std::cout << std::endl;

    return 0;
}