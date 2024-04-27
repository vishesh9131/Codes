#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
    int sockfd;
    
    // Create a socket
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    } else {
        std::cout << "Socket created successfully" << std::endl;
    }
     int serverSocket;
    
    // Create a socket
    serverSocket = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    if (serverSocket < 0) {
        std::cerr << "Error creating socket" << std::endl;
        return 1;
    } else {
        std::cout << "Socket is OK!" << std::endl;
    }
 // Bind the socket to an IP address and port number
    service.sin_family = AF_INET;
    service.sin_addr.s_addr = inet_addr("127.0.0.1");  // Replace with your desired IP address
    service.sin_port = htons(55555);  // Choose a port number

    // Use the bind function
    if (bind(serverSocket, reinterpret_cast<struct sockaddr*>(&service), sizeof(service)) < 0) {
        std::cerr << "bind() failed" << std::endl;
        close(serverSocket);
        return 1;
    } else {
        std::cout << "bind() is OK!" << std::endl;
    }    

        // Listen for incoming connections
    if (listen(serverSocket, backlog) < 0) {
        std::cerr << "Error listening on socket" << std::endl;
        return 1;
    } else {
        std::cout << "Listening for new connections..." << std::endl;
    }
    // Accept incoming connection
    acceptSocket = accept(serverSocket, nullptr, nullptr);
    if (acceptSocket < 0) {
        std::cerr << "Error accepting connection" << std::endl;
        return 1;
    } else {
        std::cout << "Connection accepted!" << std::endl;
    }

    // Send data
    const char* message = "Hello from server!";
    send(acceptSocket, message, strlen(message), 0);

    // Receive data
    int bytesReceived = recv(acceptSocket, buffer, sizeof(buffer), 0);
    if (bytesReceived < 0) {
        std::cerr << "Error receiving data" << std::endl;
    } else {
        buffer[bytesReceived] = '\0'; // Null-terminate the received data
        std::cout << "Received: " << buffer << std::endl;
    }

    // Close the sockets
    close(acceptSocket);
    close(serverSocket);


    return 0;
}

