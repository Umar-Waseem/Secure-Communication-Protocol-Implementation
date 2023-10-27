import os
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

class DHE:
    def __init__(self):
        # Generate DHE parameters and private key
        self.parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
        self.private_key = self.parameters.generate_private_key()
    
    def get_public_key(self):
        # Get the public key to send to the other party
        return self.private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    def generate_shared_key(self, peer_public_key):
        # Generate a shared key using the peer's public key
        peer_public_key = serialization.load_pem_public_key(peer_public_key, backend=default_backend())
        shared_key = self.private_key.exchange(peer_public_key)
        return shared_key

# Example of how to use the DHEKeyExchange class on the client and server side:

# On the client side:
# dhe_client = DHEKeyExchange()
# client_public_key = dhe_client.get_public_key()

# On the server side:
# dhe_server = DHEKeyExchange()
# server_public_key = dhe_server.get_public_key()

# On both sides, exchange public keys and then generate the shared key:
# shared_key_client = dhe_client.generate_shared_key(server_public_key)
# shared_key_server = dhe_server.generate_shared_key(client_public_key)
