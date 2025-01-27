import random
from crypto.number_theory import is_prime, mod_inverse

class RSA:
    """Represents the RSA (Rivest-Shamir-Adleman) algorithm."""

    def __init__(self, key_size=1024):
        """
        Initialize the RSA algorithm with a specified key size.

        Args:
            key_size (int): The size of the RSA key in bits.
        """
        self.key_size = key_size

    def generate_keys(self):
        """
        Generate RSA public and private keys.

        Returns:
            tuple: The generated private key and public key.
        """
        p = self.generate_prime()
        q = self.generate_prime()
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.choose_e(phi)
        d = mod_inverse(e, phi)
        return (d, n), (e, n)

    def generate_prime(self):
        """
        Generate a prime number of the specified key size.

        Returns:
            int: The generated prime number.
        """
        while True:
            prime_candidate = random.getrandbits(self.key_size // 2)
            if is_prime(prime_candidate):
                return prime_candidate

    def choose_e(self, phi):
        """
        Choose a suitable value for e.

        Args:
            phi (int): The value of phi(n).

        Returns:
            int: The chosen value for e.
        """
        e = 65537  # Commonly used prime number for e
        if phi % e == 0:
            for i in range(3, phi, 2):
                if phi % i != 0 and is_prime(i):
                    return i
        return e

    def encrypt(self, plaintext, public_key):
        """
        Encrypt the plaintext using the provided public key.

        Args:
            plaintext (str): The plaintext to encrypt.
            public_key (tuple): The public key (e, n).

        Returns:
            list: The encrypted ciphertext.
        """
        e, n = public_key
        plaintext_bytes = [ord(char) for char in plaintext]
        ciphertext = [pow(byte, e, n) for byte in plaintext_bytes]
        return ciphertext

    def decrypt(self, ciphertext, private_key):
        """
        Decrypt the ciphertext using the provided private key.

        Args:
            ciphertext (list): The ciphertext to decrypt.
            private_key (tuple): The private key (d, n).

        Returns:
            str: The decrypted plaintext.
        """
        d, n = private_key
        plaintext_bytes = [pow(byte, d, n) for byte in ciphertext]
        plaintext = ''.join(chr(byte) for byte in plaintext_bytes)
        return plaintext
