#include <iostream>
#include <thread>
#include <vector>
#include <cstring>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

const int PORT = 8080;

// Helper to read exactly N bytes
bool read_n(int fd, char* buffer, size_t n) {
    size_t total = 0;
    while (total < n) {
        ssize_t bytes = recv(fd, buffer + total, n - total, 0);
        if (bytes <= 0) return false; // client disconnected or error
        total += bytes;
    }
    return true;
}

void handle_client(int client_fd) {
    std::cout << "Client connected. FD: " << client_fd << "\n";

    while (true) {
        uint32_t len_net;

	ssize_t bytes = recv(client_fd, &len_net, sizeof(len_net), 0 );
	std::cout << "Bytes received: " << bytes << std::endl;
        if ( bytes < 0 ) { //read_n(client_fd, (char*)&len_net, sizeof(len_net))) {
            std::cout << "Client disconnected (during length read):" << ntohl(len_net) << "\n";
            break;
        }

        uint32_t len = ntohl(len_net);
        if (len > 4096) {
            std::cerr << "Client sent message too large!\n";
            break;
        }

        std::vector<char> buffer(len);
        if (!read_n(client_fd, buffer.data(), len)) {
            std::cout << "Client disconnected (during data read)\n";
            break;
        }

        std::string msg(buffer.begin(), buffer.end());
        std::cout << "Received message: " << msg << "\n";

        // Echo response using same framing
        std::string response = "Echo: " + msg;
        uint32_t res_len = htonl(response.size());
        send(client_fd, &res_len, sizeof(res_len), 0);
        send(client_fd, response.data(), response.size(), 0);
    }

    close(client_fd);
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
