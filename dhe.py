from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend

class DHE:

    @staticmethod
    def generate_dh_key_pair():
    # Generate a Diffie-Hellman key pair
        parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
        private_key = parameters.generate_private_key()
        public_key = private_key.public_key()
        return private_key, public_key

    @staticmethod
    def dh_key_exchange(private_key, public_key):
        # Perform a Diffie-Hellman key exchange
        shared_key = private_key.exchange(public_key)
        return shared_key