import socket
import ssl
from flask import Flask, request, send_file
from dhe import DHE
from hashing import SHA

def sendmsg(msg):
    msg = msg.encode()
    client_socket.send(msg)

def recvmsg():
    client_msg = client_socket.recv(1024).decode()
    return client_msg


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
ssl_context.load_cert_chain(certfile='server.crt', keyfile='server.key')  

# Wrap the client_socket with SSL
client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

###################################
###### 2. SENDING SERVER HELLO ###### 
###################################

client_msg = recvmsg()

print("(Server) client message: ", client_msg)

supported_cipher_suites = client_msg.split(",")
print("(Server) Supported cipher suites: ", supported_cipher_suites)

encryption_type='symmetric'

# app = Flask(__name__)

# @app.route('/')
# def main():
#     return send_file('encryption_choice.html')

# @app.route('/process_form', methods=['POST'])
# def process_form():
#     global encryption_type 
#     et = request.form.get('encryptionType')
#     encryption_type = et
#     return send_file('process_form.html')

# app.run(host='0.0.0.0', port=5000, debug=True)


if encryption_type=='asymmetric':
    CHOSEN_CIPHER_SUITE = supported_cipher_suites[0]
else:
    CHOSEN_CIPHER_SUITE = supported_cipher_suites[1]
    dhe_server = DHE.DHE()
    server_public_key = dhe_server.get_public_key()



CHOSEN_CIPHER_SUITE = supported_cipher_suites[1]


print("(Server) Server Chose cipher suite: ", CHOSEN_CIPHER_SUITE)

server_msg = CHOSEN_CIPHER_SUITE 

sendmsg(server_msg)

while True:
    server_input = input("(Server) Type your message (or 'exit' to quit): ")
    if server_input.lower() == 'exit':
        break  
    else:
       hashed_server = SHA.sha256(server_input)



client_socket.close()
server_socket.close()
