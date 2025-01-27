import unittest
from crypto.encryption import Encryption
from crypto.decryption import Decryption
from group_theory.galois_field import GaloisField

class TestCrypto(unittest.TestCase):
    def setUp(self):
        elements = {0, 1, 2, 3}
        addition = lambda a, b: (a + b) % 4
        multiplication = lambda a, b: (a * b) % 4
        self.galois_field = GaloisField(elements, addition, multiplication)
        self.encryption = Encryption(self.galois_field)
        self.decryption = Decryption(self.galois_field)

    def test_key_generation(self):
        encryption_key = self.encryption.generate_key()
        decryption_key = self.decryption.generate_key()
        self.assertIsNotNone(encryption_key)
        self.assertIsNotNone(decryption_key)

    def test_encryption_decryption(self):
        plaintext = "hello"
        key = self.encryption.generate_key()
        ciphertext = self.encryption.encrypt(plaintext, key)
        decrypted_text = self.decryption.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

if __name__ == "__main__":
    unittest.main()
