#include "PhysicsWorld.h"

int main() {
    // 1. Initialize OpenGL/Windowing here (omitted for brevity)
    
    // 2. Initialize Physics World
    PhysicsWorld world;

    // Create two spheres on a collision course
    // Position, Radius, Mass, Restitution
    PhysicsSphere sphere1(glm::vec3(-5.0f, 0.0f, 0.0f), 1.0f, 2.0f, 0.8f);
    PhysicsSphere sphere2(glm::vec3( 5.0f, 0.0f, 0.0f), 1.5f, 4.0f, 0.8f);

    // Give them velocity moving towards each other
    sphere1.velocity = glm::vec3(3.0f, 0.0f, 0.0f);
    sphere2.velocity = glm::vec3(-2.0f, 0.0f, 0.0f);

    world.addSphere(&sphere1);
    world.addSphere(&sphere2);

    float deltaTime = 0.016f; // Assuming ~60 FPS

    // 3. Main Game Loop
    bool isRunning = true;
    while (isRunning) {
        // --- Input Handling ---
        // (Check for window close, etc.)

        // --- Physics Update ---
        world.step(deltaTime);

        // --- OpenGL Rendering ---
        // glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        
        // sphere1.draw();
        // sphere2.draw();

        // Swap buffers and poll events
    }

    return 0;
}