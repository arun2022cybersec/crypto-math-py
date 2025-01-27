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

    def test_aes_key_expansion(self):
        key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x9f, 0x24, 0x30, 0xc0, 0x8d]
        expanded_key = self.encryption.aes.key_expansion(key)
        self.assertEqual(len(expanded_key), 44)  # AES-128 should have 44 words in the expanded key

    def test_aes_encryption_decryption(self):
        plaintext = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
        key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x9f, 0x24, 0x30, 0xc0, 0x8d]
        ciphertext = self.encryption.aes.encrypt(plaintext, key)
        decrypted_text = self.decryption.aes.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

if __name__ == "__main__":
    unittest.main()
