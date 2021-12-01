#pragma once

#include <vector>
#include "vector.h"

class MultiVector {
public:
    std::vector<Vector> m_vectors;

    MultiVector(std::vector<Vector>& vectors);
};