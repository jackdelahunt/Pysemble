#include "lib/person.h"
#include <iostream>

int main() {
    auto p = Person();
    std::cout << p.age;
    return 0;
}