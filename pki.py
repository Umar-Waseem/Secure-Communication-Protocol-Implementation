from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils

class SimplePKI:

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_key_pair(self):
        # Generate an RSA key pair
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        self.public_key = self.private_key.public_key()

    def sign(self, message):
        # Sign a message using the private key
        if not self.private_key:
            raise ValueError("Private key not generated")
        signature = self.private_key.sign(
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return signature

    def verify(self, message, signature):
        # Verify a message's signature using the public key
        if not self.public_key:
            raise ValueError("Public key not available")
        try:
            self.public_key.verify(
                signature,
                message,
                padding.PKCS1v15(),
                hashes.SHA256()
            )
            return True  # Signature is valid
        except:
            return False  # Signature is invalid

# an example on how to use this
# if __name__ == "__main__":
#     pki = SimplePKI()

#     # Generate a key pair
#     pki.generate_key_pair()

#     message = b"Hello, PKI!"

#     # Sign the message
#     signature = pki.sign(message)

#     # Verify the signature
#     is_valid = pki.verify(message, signature)

#     if is_valid:
#         print("Signature is valid.")
#     else:
#         print("Signature is not valid.")
