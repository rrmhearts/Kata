#include "zmq.hpp"
#include <iostream>
#include <fstream>
#include <thread>
#include "schema.hpp"

// Mock function for system data
SystemState get_local_state() {
    return {"Workstation-Alpha", 12.5, 8.2, std::time(nullptr)};
}

int main() {
    // 1. Load Config
    std::ifstream f("config.json");
    Config cfg = json::parse(f);

    // 2. Setup ZeroMQ Publisher
    zmq::context_t context(1);
    zmq::socket_t publisher(context, zmq::socket_type::pub);
    publisher.bind(cfg.pub_endpoint);

    std::cout << "Producer started. Publishing on " << cfg.pub_endpoint << "..." << std::endl;

    while (true) {
        // Get data
        SystemState state = get_local_state();
        
        // Serialize to JSON string
        std::string payload = json(state).dump();

        // Send (Topic: "SYS_STATS")
        zmq::message_t topic("SYS_STATS", 9);
        zmq::message_t message(payload.size());
        memcpy(message.data(), payload.data(), payload.size());

        publisher.send(topic, zmq::send_flags::sndmore);
        publisher.send(message, zmq::send_flags::none);

        std::this_thread::sleep_for(std::chrono::milliseconds(cfg.update_interval_ms));
    }
    return 0;
}