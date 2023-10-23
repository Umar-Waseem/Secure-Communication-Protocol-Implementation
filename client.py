import socket


####### SOCKET CREATION ######

# lets create a socket for client server communication
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connecting to the server which lives on the localhost:12345
server_address = ('localhost', 12345)
client_socket.connect(server_address)

###### SENDING CLIENT HELLO ###### (part 1 of 3 way handshake)

# supported cipher suites
cipher_suites = [
    "TLS_RSA_WITH_AES_256_CBC_SHA256",
    "TLS_DHE_WITH_AES_256_CBC_SHA256",
    "TLS_RSA_WITH_AES_128_CBC_SHA256",
    "TLS_DHE_WITH_AES_128_CBC_SHA256"
]
cipher_suites = ",".join(cipher_suites)

client_hello_message = cipher_suites
print("(Client) ClientHello message to the server: ", client_hello_message)

# convert the message to bytes
client_hello_message = client_hello_message.encode()

# Send the "ClientHello" message to the server
client_socket.send(client_hello_message)

# Receive the "ServerHello" message from the server
server_hello_message = client_socket.recv(1024)
server_hello_message = server_hello_message.decode()
print("(Client) ServerHello message from the server: ", server_hello_message)

# Close the connection
client_socket.close()





