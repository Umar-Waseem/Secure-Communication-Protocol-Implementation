import socket

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization



# generate public and private keys

def get_public_private_keys():

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )

    public_key = private_key.public_key()

    return private_key, public_key


def save_public_key(public_key):
    pem = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    )

    with open("public_key.pem", "wb") as public_key_file:
        public_key_file.write(pem)


def save_private_key(private_key):
    pem = private_key.private_bytes(
        encoding=Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    )

    with open("private_key.pem", "wb") as private_key_file:
        private_key_file.write(pem)



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
