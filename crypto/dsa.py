from group_theory.galois_field import GaloisField

class DSA(GaloisField):
    """Represents the Digital Signature Algorithm (DSA) using Galois fields."""

    def __init__(self, elements, addition, multiplication, p, q, g):
        """
        Initialize the DSA algorithm with elements, addition, multiplication operations, and DSA parameters.

        Args:
            elements (set): The set of elements in the Galois field.
            addition (callable): The addition operation for the Galois field.
            multiplication (callable): The multiplication operation for the Galois field.
            p (int): A prime number.
            q (int): A prime divisor of p-1.
            g (int): A generator of the subgroup of order q in the multiplicative group of integers modulo p.
        """
        super().__init__(elements, addition, multiplication)
        self.p = p
        self.q = q
        self.g = g

    def generate_keys(self):
        """
        Generate a pair of private and public keys for DSA.

        Returns:
            tuple: The private key and the public key.
        """
        private_key = random.randint(1, self.q - 1)
        public_key = pow(self.g, private_key, self.p)
        return private_key, public_key

    def sign(self, message, private_key):
        """
        Sign a message using the provided private key.

        Args:
            message (str): The message to sign.
            private_key (int): The private key.

        Returns:
            tuple: The signature (r, s).
        """
        k = random.randint(1, self.q - 1)
        r = pow(self.g, k, self.p) % self.q
        k_inv = pow(k, -1, self.q)
        hash_value = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
        s = (k_inv * (hash_value + private_key * r)) % self.q
        return r, s

    def verify(self, message, signature, public_key):
        """
        Verify a message signature using the provided public key.

        Args:
            message (str): The message to verify.
            signature (tuple): The signature (r, s).
            public_key (int): The public key.

        Returns:
            bool: True if the signature is valid, False otherwise.
        """
        r, s = signature
        if not (0 < r < self.q and 0 < s < self.q):
            return False
        w = pow(s, -1, self.q)
        hash_value = int.from_bytes(hashlib.sha256(message.encode()).digest(), 'big')
        u1 = (hash_value * w) % self.q
        u2 = (r * w) % self.q
        v = ((pow(self.g, u1, self.p) * pow(public_key, u2, self.p)) % self.p) % self.q
        return v == r
