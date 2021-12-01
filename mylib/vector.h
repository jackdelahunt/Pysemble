#pragma once

class Vector{
public:
    int x;
    int y;

    Vector(int x, int y);
    void add(Vector& other);
    void sub(Vector& other);
};