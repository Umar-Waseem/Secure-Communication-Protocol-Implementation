import socket

###### SOCKET CREATION ######

# creating a socket for client server communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port so server can listen to it
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# listen for incoming connections
server_socket.listen(1)

print("(Server) Waiting for a connection...")

# accept a connection from the client
client_socket, client_address = server_socket.accept()
print("(Server) Connected to", client_address)

###### SENDING SERVER HELLO ###### (part 2 of 3 way handshake)

# Receive the "ClientHello" message from the client
client_hello_message = client_socket.recv(1024)
print("(Server) ClientHello message from the client: ", client_hello_message)

# convert client_hello_message to string
client_hello_message = client_hello_message.decode()
print("(Server) decoded client_hello_message: ", client_hello_message)

# Extract supported cipher suites from the "ClientHello" message (for further processing) and create a list
supported_cipher_suites = client_hello_message.split(",")
print("(Server) Supported cipher suites: ", supported_cipher_suites)

# Choose the cipher suite to use
CHOSEN_CIPHER_SUITE = supported_cipher_suites[0]
print("(Server) Server Chose cipher suite: ", CHOSEN_CIPHER_SUITE)

# Create the "ServerHello" message
server_hello_message = CHOSEN_CIPHER_SUITE  # Chosen cipher suite

# Send the "ServerHello" message to the client
server_hello_message = server_hello_message.encode()
client_socket.send(server_hello_message)

# Close the connection
client_socket.close()
server_socket.close()
