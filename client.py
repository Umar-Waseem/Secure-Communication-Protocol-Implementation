## Client Implementation - Assignment 2 - Secure Communication Protocol

## i200762
## Muhammad Umar Waseem

## i202473
## Muhammad Huzaifa

import socket

# PKI
# RSA
# SHA256
# AES
# DHE

supported_cipher_suites = [
    "TLS_RSA_WITH_AES_256_CBC_SHA256",
    "TLS_DHE_WITH_AES_256_CBC_SHA256",
    "TLS_RSA_WITH_AES_128_CBC_SHA256",
    "TLS_DHE_WITH_AES_128_CBC_SHA256"
]


def encrypt_message(message, public_key):
    # encrypt the message using the public key
    return message

def decrypt_message(message, private_key):
    # decrypt the message using the private key
    return message

def generate_session_key():
    session_key = ""
    return session_key

# generate a public/private key pair
public_key = ""
private_key = ""

# generate a session key
session_key = generate_session_key()

# first we create a socket through which this client will reach/connect a target server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# the server's address and port to which we want to connect - runs on local host on port 12345
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# send and receive data from the server
# this is an infinite loop - it will run until the connection is closed
while True:

    # user input is sent to the server
    message = input("Enter a message (or 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    client_socket.send(message.encode('utf-8'))

    # receive the server's response
    data = client_socket.recv(1024).decode('utf-8')
    print("Server response:", data)

# close up the connection and release resources
client_socket.close()
