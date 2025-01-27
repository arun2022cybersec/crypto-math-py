class DES:
    """Represents the DES (Data Encryption Standard) algorithm."""

    def __init__(self):
        """Initialize the DES algorithm with predefined parameters."""
        self.key_size = 8  # DES key size is 8 bytes (64 bits)
        self.block_size = 8  # DES block size is 8 bytes (64 bits)
        self.num_rounds = 16  # DES uses 16 rounds of processing

    def generate_key(self):
        """Generate a random key for DES encryption."""
        import os
        return os.urandom(self.key_size)

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            bytes: The encrypted ciphertext.
        """
        from Crypto.Cipher import DES
        from Crypto.Util.Padding import pad

        cipher = DES.new(key, DES.MODE_ECB)
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
        from Crypto.Cipher import DES
        from Crypto.Util.Padding import unpad

        cipher = DES.new(key, DES.MODE_ECB)
        decrypted_padded_plaintext = cipher.decrypt(ciphertext)
        plaintext = unpad(decrypted_padded_plaintext, self.block_size).decode()
        return plaintext
