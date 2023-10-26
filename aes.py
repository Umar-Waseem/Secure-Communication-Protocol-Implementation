from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


class AES:

    @staticmethod
    def aes256_encrypt( key, message):
        # Encrypt a message using AES-256
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(message) + encryptor.finalize()
        return ciphertext

    @staticmethod
    def aes256_decrypt(self, key, ciphertext):
        # Decrypt a message using AES-256
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()
        message = decryptor.update(ciphertext) + decryptor.finalize()
        return message