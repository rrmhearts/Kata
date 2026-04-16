
#include <iostream>

struct S { int i; };

int use_s() {
    static_assert(sizeof(S) == sizeof(int));
    S s{15};
    // interpet struct as int
    int &i = reinterpret_cast<int&>(s);
    i = 23;
    return s.i;
}

int use_int() {
    static_assert(sizeof(int) == sizeof(int));
    int s{15};
    int &i = reinterpret_cast<int&>(s);
    i = 23;
    return s;
}
int main() {
    std::cout << use_s() << std::endl;
    std::cout << use_int() << std::endl;
    return 0;
}