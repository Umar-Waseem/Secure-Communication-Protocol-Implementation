import socket
import webbrowser
import os
import ssl

###################################
####### SOCKET CREATION ######
###################################

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 12345)
client_socket.connect(server_address)

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

# Wrap the client_socket with SSL
ssl_context = ssl.create_default_context(cafile="server.crt")
client_socket = ssl_context.wrap_socket(client_socket, server_hostname='localhost')

###################################
###### 1. SENDING CLIENT HELLO ######
###################################

supported_cipher_suites = [
    "TLS_RSA_WITH_AES_256_CBC_SHA256", # AES for symmetric encryption, RSA for key exchange, SHA256 for hashing
    "TLS_DHE_WITH_AES_256_CBC_SHA256", # DHE(deffered diffie-hellman exchange) for key exchange, AES for symmetric encryption, SHA256 for hashing
]
supported_cipher_suites = ",".join(supported_cipher_suites)

client_hello_message = supported_cipher_suites
print("(Client) ClientHello message to the server: ", client_hello_message)
client_hello_message = client_hello_message.encode()
client_socket.send(client_hello_message)

server_hello_message = client_socket.recv(1024)
server_hello_message = server_hello_message.decode()
print("(Client) ServerHello message from the server: ", server_hello_message)

# get request to server simple example which gives an html ui file
client_socket.send("GET / HTTP/1.1\r\n".encode())
data = client_socket.recv(1024)
print(data.decode())

# Save the HTML content to a local file
with open("received_file.html", "wb") as html_file:
    html_file.write(data)

file_url = os.path.abspath("received_file.html")
webbrowser.open("file://{}".format(file_url))

client_socket.close()



