#pragma once
#include <nlohmann/json.hpp>
#include <string>
#include <vector>

using json = nlohmann::json;

// The data struct we want to exchange
struct SystemState {
    std::string hostname;
    double cpu_usage;    // percentage
    double ram_used_gb;
    long timestamp;

    // Macro to automate JSON conversion
    NLOHMANN_DEFINE_TYPE_INTRUSIVE(SystemState, hostname, cpu_usage, ram_used_gb, timestamp)
};

// Configuration file format
struct Config {
    std::string pub_endpoint; // e.g., "tcp://*:5555"
    std::string sub_endpoint; // e.g., "tcp://localhost:5555"
    int update_interval_ms;

    NLOHMANN_DEFINE_TYPE_INTRUSIVE(Config, pub_endpoint, sub_endpoint, update_interval_ms)
};