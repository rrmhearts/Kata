#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <fstream>
#include <tuple>
#include "json.hpp" // nlohmann/json

using json = nlohmann::json;

// --- Simplified DIS Enumerations ---
enum class EntityType {
    UNKNOWN,
    PLANE,
    SAM,
    MISSILE
};

EntityType stringToType(const std::string& typeStr) {
    if (typeStr == "PLANE") return EntityType::PLANE;
    if (typeStr == "SAM") return EntityType::SAM;
    if (typeStr == "MISSILE") return EntityType::MISSILE;
    return EntityType::UNKNOWN;
}

std::string typeToString(EntityType type) {
    switch (type) {
        case EntityType::PLANE: return "PLANE";
        case EntityType::SAM: return "SAM";
        case EntityType::MISSILE: return "MISSILE";
        default: return "UNKNOWN";
    }
}

// --- DIS Identifiers ---
struct EntityID {
    int siteId;
    int appId;
    int entityNum;

    // Required to use EntityID as a key in std::map
    bool operator<(const EntityID& other) const {
        return std::tie(siteId, appId, entityNum) < std::tie(other.siteId, other.appId, other.entityNum);
    }
    
    std::string toString() const {
        return "[" + std::to_string(siteId) + ":" + std::to_string(appId) + ":" + std::to_string(entityNum) + "]";
    }
};

// --- Entity Class ---
class Entity {
public:
    EntityID id;
    EntityType type;
    double x, y;   // 2D Position
    double vx, vy; // 2D Velocity

    Entity(EntityID id, EntityType type, double x, double y, double vx, double vy)
        : id(id), type(type), x(x), y(y), vx(vx), vy(vy) {}

    // Kinematic update: move the entity based on velocity
    void updatePosition(double timeStep) {
        x += vx * timeStep;
        y += vy * timeStep;
    }
};

// --- Simulation Service ---
class DisSimulationService {
private:
    int exerciseId;
    std::map<EntityID, Entity> entities;

public:
    DisSimulationService() : exerciseId(0) {}

    // Load state from JSON config
    bool loadConfig(const std::string& filename) {
        std::ifstream file(filename);
        if (!file.is_open()) {
            std::cerr << "Failed to open config file." << std::endl;
            return false;
        }

        json config;
        file >> config;

        exerciseId = config["exercise_id"];
        std::cout << "Loading Exercise ID: " << exerciseId << std::endl;

        for (const auto& entJson : config["entities"]) {
            EntityID id = {entJson["site_id"], entJson["app_id"], entJson["entity_num"]};
            EntityType type = stringToType(entJson["type"]);
            
            entities.emplace(id, Entity(
                id, type, 
                entJson["x"], entJson["y"], 
                entJson["vx"], entJson["vy"]
            ));
        }
        return true;
    }

    // Step the simulation forward
    void tick(double timeStep) {
        for (auto& pair : entities) {
            pair.second.updatePosition(timeStep);
        }
    }

    // Broadcast "Entity State PDUs" to console
    void printState(int time) {
        std::cout << "\n--- Time: " << time << "s | Exercise: " << exerciseId << " ---" << std::endl;
        for (const auto& pair : entities) {
            const Entity& e = pair.second;
            std::cout << "ID: " << e.id.toString() 
                      << " | Type: " << typeToString(e.type)
                      << " | Pos: (" << e.x << ", " << e.y << ")" << std::endl;
        }
    }
};

// --- Main Execution ---
int main() {
    DisSimulationService simService;

    if (!simService.loadConfig("config.json")) {
        return 1;
    }

    simService.printState(0); // Initial State

    // Run a brief simulation loop for 3 "ticks"
    for (int t = 1; t <= 3; ++t) {
        simService.tick(1.0); // Advance 1 second per tick
        simService.printState(t);
    }

    return 0;
}