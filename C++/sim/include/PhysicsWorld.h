#pragma once
#include <vector>
#include <algorithm>
#include "PhysicsSphere.h"

class PhysicsWorld {
private:
    std::vector<PhysicsSphere*> spheres;

public:
    void addSphere(PhysicsSphere* sphere) {
        spheres.push_back(sphere);
    }

    void step(float dt) {
        // 1. Update all positions
        for (auto& sphere : spheres) {
            sphere->update(dt);
        }

        // 2. Check for collisions (brute force approach for simplicity)
        for (size_t i = 0; i < spheres.size(); ++i) {
            for (size_t j = i + 1; j < spheres.size(); ++j) {
                checkCollision(*spheres[i], *spheres[j]);
            }
        }
    }

private:
    void checkCollision(PhysicsSphere& a, PhysicsSphere& b) {
        // Calculate the vector between the two centers
        glm::vec3 collisionVector = b.position - a.position;
        
        // Calculate the distance using GLM
        float distance = glm::length(collisionVector);
        float minDistance = a.radius + b.radius;

        // If the distance is less than the sum of radii, they are colliding
        if (distance < minDistance) {
            resolveCollision(a, b, collisionVector, distance, minDistance);
        }
    }
    
    void resolveCollision(PhysicsSphere& a, PhysicsSphere& b, glm::vec3 collisionVector, float distance, float minDistance) {
        // 1. Calculate the collision normal (normalized direction vector)
        // Prevent division by zero if objects are at the exact same position
        glm::vec3 normal = (distance == 0.0f) ? glm::vec3(0, 1, 0) : glm::normalize(collisionVector);

        // 2. Resolve Interpenetration (Positional Correction)
        // We push the objects apart proportional to their inverse mass
        float invMassA = 1.0f / a.mass;
        float invMassB = 1.0f / b.mass;
        float penetrationDepth = minDistance - distance;
        
        // Push apart slightly to prevent sinking (using a small percentage to prevent jitter)
        const float percent = 0.2f; 
        glm::vec3 correction = (penetrationDepth / (invMassA + invMassB)) * percent * normal;
        
        a.position -= correction * invMassA;
        b.position += correction * invMassB;

        // 3. Resolve Velocity (Impulse Calculation)
        // Calculate relative velocity
        glm::vec3 relativeVelocity = b.velocity - a.velocity;

        // Calculate relative velocity in terms of the normal direction
        float velocityAlongNormal = glm::dot(relativeVelocity, normal);

        // Do not resolve if velocities are separating (objects moving apart)
        if (velocityAlongNormal > 0) return;

        // Calculate restitution (take the lowest bounciness of the two objects)
        float e = std::min(a.restitution, b.restitution);

        // Calculate impulse scalar
        float j = -(1.0f + e) * velocityAlongNormal;
        j /= (invMassA + invMassB);

        // Apply impulse vector to both objects
        glm::vec3 impulse = j * normal;
        
        a.velocity -= impulse * invMassA;
        b.velocity += impulse * invMassB;
    }
};