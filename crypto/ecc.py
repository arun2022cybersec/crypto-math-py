from group_theory.galois_field import GaloisField

class ECC(GaloisField):
    """Represents the Elliptic Curve Cryptography (ECC) algorithm using Galois fields."""

    def __init__(self, elements, addition, multiplication, a, b):
        """
        Initialize the ECC algorithm with elements, addition, multiplication operations, and curve parameters.

        Args:
            elements (set): The set of elements in the Galois field.
            addition (callable): The addition operation for the Galois field.
            multiplication (callable): The multiplication operation for the Galois field.
            a (int): The curve parameter 'a' in the equation y^2 = x^3 + ax + b.
            b (int): The curve parameter 'b' in the equation y^2 = x^3 + ax + b.
        """
        super().__init__(elements, addition, multiplication)
        self.a = a
        self.b = b

    def is_on_curve(self, x, y):
        """
        Check if a point (x, y) is on the elliptic curve.

        Args:
            x (int): The x-coordinate of the point.
            y (int): The y-coordinate of the point.

        Returns:
            bool: True if the point is on the curve, False otherwise.
        """
        return (y ** 2) % self.p == (x ** 3 + self.a * x + self.b) % self.p

    def point_addition(self, P, Q):
        """
        Perform point addition on the elliptic curve.

        Args:
            P (tuple): The first point (x1, y1).
            Q (tuple): The second point (x2, y2).

        Returns:
            tuple: The resulting point (x3, y3) after addition.
        """
        if P == Q:
            return self.point_doubling(P)
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and y1 == -y2:
            return (0, 0)
        m = (y2 - y1) * pow(x2 - x1, -1, self.p) % self.p
        x3 = (m ** 2 - x1 - x2) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def point_doubling(self, P):
        """
        Perform point doubling on the elliptic curve.

        Args:
            P (tuple): The point (x1, y1) to double.

        Returns:
            tuple: The resulting point (x3, y3) after doubling.
        """
        x1, y1 = P
        m = (3 * x1 ** 2 + self.a) * pow(2 * y1, -1, self.p) % self.p
        x3 = (m ** 2 - 2 * x1) % self.p
        y3 = (m * (x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_multiplication(self, k, P):
        """
        Perform scalar multiplication on the elliptic curve.

        Args:
            k (int): The scalar value.
            P (tuple): The point (x, y) to multiply.

        Returns:
            tuple: The resulting point (x', y') after multiplication.
        """
        R = (0, 0)
        while k:
            if k & 1:
                R = self.point_addition(R, P)
            P = self.point_doubling(P)
            k >>= 1
        return R

    def generate_keys(self):
        """
        Generate a pair of private and public keys for ECC.

        Returns:
            tuple: The private key and the public key.
        """
        private_key = random.randint(1, self.p - 1)
        public_key = self.scalar_multiplication(private_key, self.G)
        return private_key, public_key

    def encrypt(self, plaintext, public_key):
        """
        Encrypt the plaintext using the provided public key.

        Args:
            plaintext (str): The plaintext to encrypt.
            public_key (tuple): The public key.

        Returns:
            tuple: The encrypted ciphertext.
        """
        k = random.randint(1, self.p - 1)
        C1 = self.scalar_multiplication(k, self.G)
        C2 = self.point_addition(self.scalar_multiplication(k, public_key), plaintext)
        return C1, C2

    def decrypt(self, ciphertext, private_key):
        """
        Decrypt the ciphertext using the provided private key.

        Args:
            ciphertext (tuple): The ciphertext to decrypt.
            private_key (int): The private key.

        Returns:
            str: The decrypted plaintext.
        """
        C1, C2 = ciphertext
        S = self.scalar_multiplication(private_key, C1)
        plaintext = self.point_addition(C2, (S[0], -S[1]))
        return plaintext
