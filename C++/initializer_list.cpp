#include <iostream>
#include <initializer_list>
#include <vector>
#include <string>

class MyContainer {
private:
    std::vector<int> data;
public:
    // 1. Constructor using std::initializer_list
    MyContainer(std::initializer_list<int> list) : data(list) {
        std::cout << "Constructor called with " << list.size() << " elements.\n";
    }

    void print() const {
        for (int val : data) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
};

// 2. Regular function taking std::initializer_list
void printStrings(std::initializer_list<std::string> messages) {
    for (const auto& msg : messages) {
        std::cout << msg << " | ";
    }
    std::cout << std::endl;
}

int main() {
    // Initializing custom object with braced list
    MyContainer container = {10, 20, 30, 40, 50};
    container.print();

    // Calling function with braced list
    printStrings({"Hello", "Initializer", "List"});

    // Direct iteration over an initializer list
    for (int x : {1, 2, 3}) {
        std::cout << x << " ";
    }

    return 0;
}
