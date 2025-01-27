from group_theory.galois_field import GaloisField
from crypto.aes import AES
import hmac
from crypto.pbkdf2 import pbkdf2_hmac

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

    def generate_key(self, password: bytes, salt: bytes) -> bytes:
        """
        Generate a secure key for encryption using PBKDF2.

        Args:
            password (bytes): The password to derive the key from.
            salt (bytes): The salt to use in the key derivation.

        Returns:
            bytes: The generated key.
        """
        return pbkdf2_hmac('sha256', password, salt, 100000, 32)

    def encrypt(self, plaintext: str, key: bytes) -> (bytes, bytes):
        """
        Encrypt the plaintext using the provided key and generate a MAC for integrity check.

        Args:
            plaintext (str): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            tuple: The encrypted ciphertext and the message authentication code (MAC).

        Raises:
            ValueError: If the input types are invalid or the key length is incorrect.
        """
        if not isinstance(plaintext, str) or not isinstance(key, bytes):
            raise ValueError("Invalid input types for plaintext or key.")
        if len(key) != 32:
            raise ValueError("Invalid key length. Key must be 32 bytes long.")
        
        plaintext_bytes = plaintext.encode('utf-8')
        ciphertext = bytes(self.aes.encrypt(list(plaintext_bytes), list(key)))
        
        # Generate MAC for integrity check
        mac = hmac.new(key, ciphertext, 'sha256').digest()
        
        # Securely erase plaintext bytes from memory
        del plaintext_bytes
        
        return ciphertext, mac
