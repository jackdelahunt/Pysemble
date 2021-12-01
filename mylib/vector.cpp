#include "vector.h"

Vector::Vector(int x, int y) {
    this->x = x;
    this->y = y;
}

void Vector::add(Vector& other) {
    x += other.x;
    y += other.y;
}

void Vector::sub(Vector& other) {
    x -= other.x;
    y -= other.y;
}
