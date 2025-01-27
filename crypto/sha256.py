import hashlib

class SHA256:
    """Represents the SHA-256 (Secure Hash Algorithm 256-bit) algorithm."""

    def __init__(self):
        """Initialize the SHA-256 algorithm."""
        self.hasher = hashlib.sha256()

    def hash(self, data: str) -> str:
        """
        Hash the input data using SHA-256.

        Args:
            data (str): The input data to hash.

        Returns:
            str: The hexadecimal representation of the hash value.
        """
        self.hasher.update(data.encode('utf-8'))
        return self.hasher.hexdigest()
