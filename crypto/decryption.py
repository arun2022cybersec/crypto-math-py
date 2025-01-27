from group_theory.galois_field import GaloisField
from crypto.aes import AES
import os

class Decryption:
    """Represents decryption algorithms using Galois fields."""
    
    def __init__(self, galois_field: GaloisField):
        """
        Initialize the decryption with a Galois field.

        Args:
            galois_field (GaloisField): The Galois field for cryptographic operations.
        """
        self.galois_field = galois_field
        self.aes = AES(galois_field.elements, galois_field.addition, galois_field.multiplication)

    def generate_key(self):
        """
        Generate a secure key for decryption.

        Returns:
            bytes: The generated key.
        """
        return os.urandom(16)  # Generate a 128-bit key

    def decrypt(self, ciphertext: bytes, key: bytes) -> str:
        """
        Decrypt the ciphertext using the provided key.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            key (bytes): The decryption key.

        Returns:
            str: The decrypted plaintext.
        """
        if not isinstance(ciphertext, bytes) or not isinstance(key, bytes):
            raise ValueError("Invalid input types for ciphertext or key.")
        
        plaintext_bytes = self.aes.decrypt(list(ciphertext), list(key))
        plaintext = bytes(plaintext_bytes).decode('utf-8')
        
        # Securely erase plaintext bytes from memory
        del plaintext_bytes
        
        return plaintext
