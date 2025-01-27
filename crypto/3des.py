from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

class TripleDES:
    """Represents the Triple DES (3DES) algorithm."""

    def __init__(self):
        """Initialize the Triple DES algorithm with predefined parameters."""
        self.key_size = 24  # 3DES key size is 24 bytes (192 bits)
        self.block_size = 8  # 3DES block size is 8 bytes (64 bits)

    def generate_key(self):
        """Generate a random key for 3DES encryption."""
        return get_random_bytes(self.key_size)

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            bytes: The encrypted ciphertext.
        """
        cipher = DES3.new(key, DES3.MODE_ECB)
        padded_plaintext = pad(plaintext.encode(), self.block_size)
        ciphertext = cipher.encrypt(padded_plaintext)
        return ciphertext

    def decrypt(self, ciphertext, key):
        """
        Decrypt the ciphertext using the provided key.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            key (bytes): The decryption key.

        Returns:
            str: The decrypted plaintext.
        """
        cipher = DES3.new(key, DES3.MODE_ECB)
        decrypted_padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted_padded_plaintext, self.block_size).decode()
        return plaintext
