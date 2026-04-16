#include <string>
#include <iostream>

std::string get_data() {
    const char s[] = "local pointer"; // fails to print on return std::string_view
    //std::string s = "from get_data"; // fails to print on std::string_view return type
    return s; // return std::string will work fine because copied for both char[] and string

    //return "string literal from get_data"; // works fine because staticly allocated
}
int main() {
    std::string s = "Hello World!";
    std::string_view sv = s;
    std::cout << sv << std::endl;

    // gibberish
    std::cout << get_data() << std::endl;
    return 0;
}