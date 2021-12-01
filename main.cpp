#include "mylib/multi_vector.h"
#include "mylib/vector.h"
#include <iostream>

int main() {
    std::vector<Vector> vectors;
    vectors.push_back(Vector(1, 2));
    vectors.push_back(Vector(3, 4));
    MultiVector mv(vectors);
    std::cout << mv.m_vectors.size();

    return 0;
}