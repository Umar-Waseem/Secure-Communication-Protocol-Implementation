from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class HashingAlgos:

    @staticmethod
    def sha256(message):
        # Compute the SHA-256 hash of a message
        digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
        digest.update(message)
        return digest.finalize()




