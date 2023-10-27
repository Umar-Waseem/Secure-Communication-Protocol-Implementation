from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class SHA:

    @staticmethod
    def sha256(message):
        message_bytes = message.encode('utf-8')

        # Compute the SHA-256 hash of the message
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message_bytes)
        return digest.finalize()
