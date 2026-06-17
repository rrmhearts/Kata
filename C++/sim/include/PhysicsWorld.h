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
        for (auto& sphere : spheres) {
            sphere->update(dt);
        }

        for (size_t i = 0; i < spheres.size(); ++i) {
            for (size_t j = i + 1; j < spheres.size(); ++j) {
                checkCollision(*spheres[i], *spheres[j]);
            }
        }
    }

private:
    void checkCollision(PhysicsSphere& a, PhysicsSphere& b) {
        glm::vec3 collisionVector = b.position - a.position;
        float distance = glm::length(collisionVector);
        float minDistance = a.radius + b.radius;

        if (distance < minDistance) {
            resolveCollision(a, b, collisionVector, distance, minDistance);
        }
    }
    
    void resolveCollision(PhysicsSphere& a, PhysicsSphere& b, glm::vec3 collisionVector, float distance, float minDistance) {
        glm::vec3 normal = (distance == 0.0f) ? glm::vec3(0, 1, 0) : glm::normalize(collisionVector);

        float invMassA = 1.0f / a.mass;
        float invMassB = 1.0f / b.mass;
        float penetrationDepth = minDistance - distance;
        
        const float percent = 0.2f; 
        glm::vec3 correction = (penetrationDepth / (invMassA + invMassB)) * percent * normal;
        
        a.position -= correction * invMassA;
        b.position += correction * invMassB;

        glm::vec3 relativeVelocity = b.velocity - a.velocity;
        float velocityAlongNormal = glm::dot(relativeVelocity, normal);

        if (velocityAlongNormal > 0) return;

        float e = std::min(a.restitution, b.restitution);
        float j = -(1.0f + e) * velocityAlongNormal;
        j /= (invMassA + invMassB);

        glm::vec3 impulse = j * normal;
        
        a.velocity -= impulse * invMassA;
        b.velocity += impulse * invMassB;
    }
};