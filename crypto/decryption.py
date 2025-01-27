from group_theory.galois_field import GaloisField
from crypto.aes import AES
import hmac
from crypto.pbkdf2 import pbkdf2_hmac

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

    def generate_key(self, password: bytes, salt: bytes) -> bytes:
        """
        Generate a secure key for decryption using PBKDF2.

        Args:
            password (bytes): The password to derive the key from.
            salt (bytes): The salt to use in the key derivation.

        Returns:
            bytes: The generated key.
        """
        return pbkdf2_hmac('sha256', password, salt, 100000, 32)

    def decrypt(self, ciphertext: bytes, key: bytes, mac: bytes) -> str:
        """
        Decrypt the ciphertext using the provided key and verify the integrity using MAC.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            key (bytes): The decryption key.
            mac (bytes): The message authentication code for integrity check.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If the input types are invalid or the MAC verification fails.
        """
        if not isinstance(ciphertext, bytes):
            raise ValueError("Invalid input type for ciphertext. Expected bytes.")
        if not isinstance(key, bytes):
            raise ValueError("Invalid input type for key. Expected bytes.")
        if not isinstance(mac, bytes):
            raise ValueError("Invalid input type for mac. Expected bytes.")
        if len(key) != 32:
            raise ValueError("Invalid key length. Key must be 32 bytes long.")
        
        # Verify the integrity of the ciphertext using MAC
        computed_mac = hmac.new(key, ciphertext, 'sha256').digest()
        if not hmac.compare_digest(computed_mac, mac):
            raise ValueError("MAC verification failed. The ciphertext may have been tampered with.")
        
        plaintext_bytes = self.aes.decrypt(list(ciphertext), list(key))
        plaintext = bytes(plaintext_bytes).decode('utf-8')
        
        # Securely erase plaintext bytes from memory
        del plaintext_bytes
        
        return plaintext
