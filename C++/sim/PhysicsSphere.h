#ifndef PHYSICS_SPHERE_H

#include <glm/glm.hpp>
#include <glm/gtc/matrix_transform.hpp>

class PhysicsSphere {
public:
    // Spatial properties using GLM vectors
    glm::vec3 position;
    glm::vec3 velocity;
    float radius;

    // Physical properties
    float mass;
    float restitution; // Bounciness (0.0 = perfectly inelastic, 1.0 = perfectly elastic)

    // Constructor
    PhysicsSphere(glm::vec3 pos, float r, float m, float rest)
        : position(pos), velocity(0.0f), radius(r), mass(m), restitution(rest) {}

    // Update the sphere's position based on its velocity and elapsed time (dt)
    void update(float dt) {
        // Simple Euler integration
        position += velocity * dt;
    }

    // Abstracted draw function
    void draw() {
        // In a real application, you would generate a model matrix here:
        // glm::mat4 model = glm::translate(glm::mat4(1.0f), position);
        // Then pass the model matrix to your OpenGL shader and draw the sphere mesh.
    }
};
#endif