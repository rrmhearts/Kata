#include <glad/glad.h>
#include <GLFW/glfw3.h>
#include <iostream>

#include "PhysicsWorld.h"
#include "SphereRenderer.h"

// Window dimensions
const unsigned int SCR_WIDTH = 800;
const unsigned int SCR_HEIGHT = 600;

int main() {
    // --- 1. GLFW / OpenGL Initialization ---
    glfwInit();
    glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
    glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
    glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

    GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "Physics Collision Tutorial", NULL, NULL);
    if (window == NULL) {
        std::cout << "Failed to create GLFW window" << std::endl;
        glfwTerminate();
        return -1;
    }
    glfwMakeContextCurrent(window);

    // Initialize GLAD to load OpenGL function pointers
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        std::cout << "Failed to initialize GLAD" << std::endl;
        return -1;
    }

    // Enable Depth Testing so spheres render in 3D properly
    glEnable(GL_DEPTH_TEST);

    // --- 2. Initialize Physics and Renderer ---
    SphereRenderer renderer;
    PhysicsWorld world;

    // Create Spheres (Position, Radius, Mass, Restitution, Color)
    // Red Sphere
    PhysicsSphere sphere1(glm::vec3(-5.0f, 0.0f, 0.0f), 1.0f, 2.0f, 0.8f, glm::vec3(1.0f, 0.2f, 0.2f));
    // Blue Sphere (larger and heavier)
    PhysicsSphere sphere2(glm::vec3(5.0f, 0.0f, 0.0f), 1.5f, 4.0f, 0.8f, glm::vec3(0.2f, 0.3f, 1.0f));

    // Send them on a collision course
    sphere1.velocity = glm::vec3(4.0f, 0.0f, 0.0f);
    sphere2.velocity = glm::vec3(-2.0f, 0.0f, 0.0f);

    world.addSphere(&sphere1);
    world.addSphere(&sphere2);

    // Camera setup
    glm::mat4 projection = glm::perspective(glm::radians(45.0f), (float)SCR_WIDTH / (float)SCR_HEIGHT, 0.1f, 100.0f);
    glm::mat4 view = glm::lookAt(glm::vec3(0.0f, 4.0f, 15.0f), glm::vec3(0.0f, 0.0f, 0.0f), glm::vec3(0.0f, 1.0f, 0.0f));

    // Time variables for a fixed physics timestep
    float deltaTime = 0.016f; // Target ~60hz physics step
    float lastFrame = glfwGetTime();

    // --- 3. Main Game Loop ---
    while (!glfwWindowShouldClose(window)) {
        // Calculate dynamic delta time
        float currentFrame = glfwGetTime();
        float frameTime = currentFrame - lastFrame;
        lastFrame = currentFrame;

        // Input
        if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
            glfwSetWindowShouldClose(window, true);

        // Update Physics (Passing dynamic frame time ensures smooth movement)
        world.step(frameTime);

        // Render
        glClearColor(0.1f, 0.1f, 0.15f, 1.0f); // Dark grey background
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

        // Draw spheres
        renderer.draw(sphere1.position, sphere1.radius, sphere1.color, view, projection);
        renderer.draw(sphere2.position, sphere2.radius, sphere2.color, view, projection);

        // Swap buffers and poll IO events
        glfwSwapBuffers(window);
        glfwPollEvents();
    }

    // --- 4. Cleanup ---
    glfwTerminate();
    return 0;
}