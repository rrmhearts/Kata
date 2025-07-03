#include <iostream>
#include <thread>
#include <vector>
#include <cstring>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

const int PORT = 8080;

void handle_client(int client_fd) {
    char buffer[1024];
    std::cout << "Client connected. FD: " << client_fd << "\n";

    while (true) {
        std::memset(buffer, 0, sizeof(buffer));
        int bytes = recv(client_fd, buffer, sizeof(buffer) - 1, 0);
        if (bytes <= 0) {
            std::cout << "Client disconnected. FD: " << client_fd << "\n";
            break;
        }

        std::cout << "Received from client " << client_fd << ": " << buffer << "\n";

        std::string response = "Echo: ";
        response += buffer;
        send(client_fd, response.c_str(), response.size(), 0);
    }

    close(client_fd); // Clean up
}

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd == -1) {
        perror("socket");
        return 1;
    }

    int opt = 1;
    setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt)); // Reuse port

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;  // Listen on all interfaces
    server_addr.sin_port = htons(PORT);

    if (bind(server_fd, (sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("bind");
        close(server_fd);
        return 1;
    }

    if (listen(server_fd, SOMAXCONN) < 0) {
        perror("listen");
        close(server_fd);
        return 1;
    }

    std::cout << "Server listening on port " << PORT << "...\n";

    std::vector<std::thread> threads;

    while (true) {
        int client_fd = accept(server_fd, nullptr, nullptr);
        if (client_fd < 0) {
            perror("accept");
            continue;
        }

        // Detach thread so it cleans up on its own
        threads.emplace_back(std::thread(handle_client, client_fd)).detach();
    }

    // Optional: close server socket (unreachable here)
    close(server_fd);
    return 0;
}

