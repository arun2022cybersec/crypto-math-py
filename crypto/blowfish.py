from group_theory.galois_field import GaloisField

class Blowfish(GaloisField):
    """Represents the Blowfish encryption algorithm using Galois fields."""

    def __init__(self, elements, addition, multiplication):
        """
        Initialize the Blowfish algorithm with elements, addition, and multiplication operations.

        Args:
            elements (set): The set of elements in the Galois field.
            addition (callable): The addition operation for the Galois field.
            multiplication (callable): The multiplication operation for the Galois field.
        """
        super().__init__(elements, addition, multiplication)
        self.N = 16  # Number of rounds in Blowfish
        self.P = [0] * (self.N + 2)  # P-array
        self.S = [[0] * 256 for _ in range(4)]  # S-boxes

    def key_expansion(self, key):
        """
        Perform key expansion to generate subkeys.

        Args:
            key (bytes): The encryption key.

        Returns:
            None
        """
        # Key expansion logic
        key_len = len(key)
        for i in range(self.N + 2):
            self.P[i] = (self.P[i] ^ int.from_bytes(key[i % key_len:i % key_len + 4], 'big')) & 0xFFFFFFFF

        def F(x):
            h = self.S[0][x >> 24] + self.S[1][(x >> 16) & 0xFF]
            return (h ^ self.S[2][(x >> 8) & 0xFF]) + self.S[3][x & 0xFF]

        L, R = 0, 0
        for i in range(0, self.N + 2, 2):
            L, R = self.encrypt_block(L, R)
            self.P[i], self.P[i + 1] = L, R

        for i in range(4):
            for j in range(0, 256, 2):
                L, R = self.encrypt_block(L, R)
                self.S[i][j], self.S[i][j + 1] = L, R

    def encrypt_block(self, L, R):
        """
        Encrypt a single block of data.

        Args:
            L (int): Left half of the block.
            R (int): Right half of the block.

        Returns:
            tuple: The encrypted left and right halves.
        """
        for i in range(self.N):
            L = (L ^ self.P[i]) & 0xFFFFFFFF
            R = (R ^ self.F(L)) & 0xFFFFFFFF
            L, R = R, L
        L, R = R, L
        R = (R ^ self.P[self.N]) & 0xFFFFFFFF
        L = (L ^ self.P[self.N + 1]) & 0xFFFFFFFF
        return L, R

    def decrypt_block(self, L, R):
        """
        Decrypt a single block of data.

        Args:
            L (int): Left half of the block.
            R (int): Right half of the block.

        Returns:
            tuple: The decrypted left and right halves.
        """
        for i in range(self.N + 1, 1, -1):
            L = (L ^ self.P[i]) & 0xFFFFFFFF
            R = (R ^ self.F(L)) & 0xFFFFFFFF
            L, R = R, L
        L, R = R, L
        R = (R ^ self.P[1]) & 0xFFFFFFFF
        L = (L ^ self.P[0]) & 0xFFFFFFFF
        return L, R

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (bytes): The plaintext to encrypt.
            key (bytes): The encryption key.

        Returns:
            bytes: The encrypted ciphertext.
        """
        self.key_expansion(key)
        ciphertext = bytearray()
        for i in range(0, len(plaintext), 8):
            L = int.from_bytes(plaintext[i:i + 4], 'big')
            R = int.from_bytes(plaintext[i + 4:i + 8], 'big')
            L, R = self.encrypt_block(L, R)
            ciphertext.extend(L.to_bytes(4, 'big'))
            ciphertext.extend(R.to_bytes(4, 'big'))
        return bytes(ciphertext)

    def decrypt(self, ciphertext, key):
        """
        Decrypt the ciphertext using the provided key.

        Args:
            ciphertext (bytes): The ciphertext to decrypt.
            key (bytes): The decryption key.

        Returns:
            bytes: The decrypted plaintext.
        """
        self.key_expansion(key)
        plaintext = bytearray()
        for i in range(0, len(ciphertext), 8):
            L = int.from_bytes(ciphertext[i:i + 4], 'big')
            R = int.from_bytes(ciphertext[i + 4:i + 8], 'big')
            L, R = self.decrypt_block(L, R)
            plaintext.extend(L.to_bytes(4, 'big'))
            plaintext.extend(R.to_bytes(4, 'big'))
        return bytes(plaintext)
