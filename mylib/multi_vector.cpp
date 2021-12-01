#include "multi_vector.h"

MultiVector::MultiVector(std::vector<Vector>& vectors) {
    m_vectors = vectors;
}