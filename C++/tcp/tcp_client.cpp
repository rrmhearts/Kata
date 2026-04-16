#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

int main() {
    int sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd < 0) {
        perror("socket");
        return 1;
    }

    sockaddr_in server_addr{};
    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(8080);
    inet_pton(AF_INET, "127.0.0.1", &server_addr.sin_addr);

    if (connect(sock_fd, (sockaddr*)&server_addr, sizeof(server_addr)) < 0) {
        perror("connect");
        close(sock_fd);
        return 1;
    }

    const char* message = "Hello from client!";
    send(sock_fd, message, strlen(message), 0);

    char buffer[1024] = {};
    int bytes = recv(sock_fd, buffer, sizeof(buffer), 0);
    if (bytes > 0) {
        std::cout << "Server says: " << buffer << "\n";
    }

    close(sock_fd);
    return 0;
}

