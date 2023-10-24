import socket
import ssl

###################################
###### SOCKET CREATION ######
###################################

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 12345)
server_socket.bind(server_address)
# listen for incoming connections
server_socket.listen(1)

print("(Server) Waiting for a connection...")

client_socket, client_address = server_socket.accept()
print("(Server) Connected to", client_address)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')  # Replace with your certificate and key file paths

# Wrap the client_socket with SSL
client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

###################################
###### 2. SENDING SERVER HELLO ###### 
###################################

client_hello_message = client_socket.recv(1024)
print("(Server) ClientHello message from the client: ", client_hello_message)

client_hello_message = client_hello_message.decode()
print("(Server) decoded client_hello_message: ", client_hello_message)

supported_cipher_suites = client_hello_message.split(",")
print("(Server) Supported cipher suites: ", supported_cipher_suites)

# Choose the cipher suite to use
CHOSEN_CIPHER_SUITE = supported_cipher_suites[0]
print("(Server) Server Chose cipher suite: ", CHOSEN_CIPHER_SUITE)

server_hello_message = CHOSEN_CIPHER_SUITE 
server_hello_message = server_hello_message.encode()
client_socket.send(server_hello_message)

# send the html file to client
with open("index.html", "rb") as html_file:
    data = html_file.read()
    client_socket.send(data)

# Close the connection
client_socket.close()
server_socket.close()
