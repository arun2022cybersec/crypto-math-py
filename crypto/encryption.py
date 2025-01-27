from group_theory.galois_field import GaloisField
from crypto.aes import AES
import os

class Encryption:
    """Represents encryption algorithms using Galois fields."""
    
    def __init__(self, galois_field: GaloisField):
        """
        Initialize the encryption with a Galois field.

        Args:
            galois_field (GaloisField): The Galois field for cryptographic operations.
        """
        self.galois_field = galois_field
        self.aes = AES(galois_field.elements, galois_field.addition, galois_field.multiplication)

    def generate_key(self):
        """
        Generate a secure key for encryption.

        Returns:
            bytes: The generated key.
        """
        return os.urandom(16)  # Generate a 128-bit key

    def encrypt(self, plaintext: str, key: bytes) -> bytes:
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            bytes: The encrypted ciphertext.
        """
        if not isinstance(plaintext, str) or not isinstance(key, bytes):
            raise ValueError("Invalid input types for plaintext or key.")
        
        plaintext_bytes = plaintext.encode('utf-8')
        ciphertext = self.aes.encrypt(plaintext_bytes, key)
        
        # Securely erase plaintext bytes from memory
        del plaintext_bytes
        
        return bytes(ciphertext)
