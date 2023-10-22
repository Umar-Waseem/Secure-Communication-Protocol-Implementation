## Server Implementation - Assignment 2 - Secure Communication Protocol


## i200762
## Muhammad Umar Waseem

## i202473
## Muhammad Huzaifa

import socket

# first we create a socket through which an incoming client will connect
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# lets bind the socket to localhost address and port of 12345
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# listen for any incoming connections
server_socket.listen(1)  # 1 is the maximum number of queued connections

print("Server is waiting for a connection...")

# accept an incoming client connection and receive the client socket and address
client_socket, client_address = server_socket.accept()
print("Connection established with", client_address)

#  receive data from the client and send a response back
#  this is an infinite loop - it will run until the connection is closed
while True:
    
    # receive buffer data of 1024 bytes from the client
    data = client_socket.recv(1024).decode('utf-8')
    
    if not data:
        break  # No more data, connection closed

    print("Received:", data)

    # Send a response back to the client
    response = "Server received: " + data
    client_socket.send(response.encode('utf-8'))


# close up the connection and free resources
client_socket.close()
server_socket.close()
