from crypto.3des_impl import TripleDESImpl

class TripleDES:
    """Represents the Triple DES (3DES) algorithm."""

    def __init__(self):
        """Initialize the Triple DES algorithm with predefined parameters."""
        self.key_size = 24  # 3DES key size is 24 bytes (192 bits)
        self.block_size = 8  # 3DES block size is 8 bytes (64 bits)
        self.impl = TripleDESImpl()

    def generate_key(self):
        """Generate a random key for 3DES encryption."""
        return self.impl.generate_key(self.key_size)

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            bytes: The encrypted ciphertext.
        """
        return self.impl.encrypt(plaintext, key, self.block_size)

    def decrypt(self, ciphertext, key):
        """
        Decrypt the ciphertext using the provided key.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            key (bytes): The decryption key.

        Returns:
            str: The decrypted plaintext.
        """
        return self.impl.decrypt(ciphertext, key, self.block_size)
