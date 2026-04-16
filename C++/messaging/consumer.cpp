#include "zmq.hpp"
#include <iostream>
#include <fstream>
#include "schema.hpp"

int main() {
    // 1. Load Config
    std::ifstream f("config.json");
    Config cfg = json::parse(f);

    // 2. Setup ZeroMQ Subscriber
    zmq::context_t context(1);
    zmq::socket_t subscriber(context, zmq::socket_type::sub);
    subscriber.connect(cfg.sub_endpoint);
    
    // Subscribe specifically to system stats
    subscriber.set(zmq::sockopt::subscribe, "SYS_STATS");

    std::cout << "Consumer connected to " << cfg.sub_endpoint << ". Waiting for data..." << std::endl;

    while (true) {
        zmq::message_t topic;
        zmq::message_t message;

        // Receive topic and then payload
        auto res1 = subscriber.recv(topic, zmq::recv_flags::none);
        auto res2 = subscriber.recv(message, zmq::recv_flags::none);

        // Convert back to Struct
        std::string json_str(static_cast<char*>(message.data()), message.size());
        SystemState state = json::parse(json_str);

        // Usage
        std::cout << "[" << state.timestamp << "] " << state.hostname 
                  << " -> CPU: " << state.cpu_usage << "%, RAM: " 
                  << state.ram_used_gb << "GB" << std::endl;
    }
    return 0;
}