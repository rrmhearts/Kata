#pragma once
#include <glm/glm.hpp>

class PhysicsSphere {
public:
    // Spatial properties using GLM vectors
    glm::vec3 position;
    glm::vec3 velocity;
    glm::vec3 gravity = glm::vec3(0.0f, -9.8f, 0.0f);
    float radius;

    // Physical properties
    float mass;
    float restitution; // Bounciness (0.0 = perfectly inelastic, 1.0 = perfectly elastic)
    glm::vec3 color; // New: Added for rendering


    // Constructor
    PhysicsSphere(glm::vec3 pos, float r, float m, float rest, glm::vec3 col)
        : position(pos), velocity(0.0f), radius(r), mass(m), restitution(rest), color(col) {}

    // Update the sphere's position based on its velocity and elapsed time (dt)
    void update(float dt) {
        // Simple Euler integration
        velocity += gravity * dt;
        position += velocity * dt;
    }

    // Abstracted draw function
    // This is absconded by SphereRenderer
    //void draw() {
        // In a real application, you would generate a model matrix here:
        // glm::mat4 model = glm::translate(glm::mat4(1.0f), position);
        // Then pass the model matrix to your OpenGL shader and draw the sphere mesh.
    //}
};