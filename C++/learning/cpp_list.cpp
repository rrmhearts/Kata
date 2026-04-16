#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <memory>
#include <algorithm>


void write_log() {
    std::ofstream file("log.txt"); // Opens file
    file << "Log entry\n";         // Writes to file
}                                  // File is closed automatically here

void increment(int& x) {
	x++;
}

int main() {
    int* ptr = nullptr;
    auto x = 5;            // int
    auto name = std::string("John"); // std::string
    increment(x);

    ptr = &x;
    std::cout << *ptr << std::endl;

    std::vector<std::string> items = { "apple", "banana", "cherry" };
    for (const auto& item : items) {
        std::cout << item << std::endl; //"\n";
    }

    write_log();

    std::unique_ptr<int> p = std::make_unique<int>(42);

    std::vector<int> v = {1, 2, 3};
    v.push_back(*p);
    
    for (int x : v) {
        std::cout << x << "\n";
    }

    // Lambda functions
    auto square = [](int x) { return x * x; };
    std::cout << square(5) << "\n";  // 25
    
    std::vector<int> nums = {1, 2, 3, 4};
    std::sort(nums.begin(), nums.end(), [](int a, int b) {
        return a > b;
    });
    for (int x : nums) std::cout << x << " ";
    std::cout << "\n";

    return 0;
}

