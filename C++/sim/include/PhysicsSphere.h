#pragma once
#include <glm/glm.hpp>

class PhysicsSphere {
public:
    glm::vec3 position;
    glm::vec3 velocity;
    float radius;
    float mass;
    float restitution;
    glm::vec3 color; // New: Added for rendering

    PhysicsSphere(glm::vec3 pos, float r, float m, float rest, glm::vec3 col)
        : position(pos), velocity(0.0f), radius(r), mass(m), restitution(rest), color(col) {}

    void update(float dt) {
        position += velocity * dt;
    }
};