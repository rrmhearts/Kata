#include <iostream>
#include <cstring>
#include <unistd.h>
#include <arpa/inet.h>

// Sends a message with length prefix
void send_message(int sock_fd, const std::string& msg) {
    uint32_t len = htonl(msg.size());
    std::cout << "sending length: " << msg.size() << " of size " << sizeof(len) << std::endl;
    send(sock_fd, &len, sizeof(len), 0);
    std::cout << "sending message: " << msg << std::endl;
    send(sock_fd, msg.c_str(), msg.size(), 0);
}


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
//    send(sock_fd, message, strlen(message), 0);
//    send_message(int sock_fd, const std::string& msg)
    send_message(sock_fd, message);

    uint32_t len_resp;
    char buffer[1024] = { 0 };
    recv(sock_fd, &len_resp, sizeof(len_resp), 0);
    std::cout << "Client received resp len: " << ntohl(len_resp) << std::endl;
    int bytes = recv(sock_fd, buffer, sizeof(buffer), 0);
    if (bytes >= 0) {
        std::cout << "Server says: " << buffer << "\n";
    }

    close(sock_fd);
    return 0;
}

