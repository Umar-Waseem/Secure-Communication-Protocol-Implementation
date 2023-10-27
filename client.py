import socket
import webbrowser
import os
import ssl


def sendmsg(msg):
    msg = msg.encode()
    client_socket.send(msg)

def recvmsg():
    server_msg= client_socket.recv(1024).decode()
    return server_msg


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
    "TLS_RSA_WITH_AES_256_CBC_SHA256",
    "TLS_DHE_WITH_AES_256_CBC_SHA256",
]
supported_cipher_suites = ",".join(supported_cipher_suites)

client_msg = supported_cipher_suites

print("(Client) message to the server: ", client_msg)

sendmsg(client_msg)

server_msg = recvmsg()
print("(Client) message from the server: ", server_msg)


client_socket.close()



