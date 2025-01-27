import unittest

from .encryption import Encryption
from .decryption import Decryption
from ..group_theory.galois_field import GaloisField
from .des import DES
from .rsa import RSA
from .3des import TripleDES
from .blowfish import Blowfish
from .twofish import Twofish
from .ecc import ECC
from .dsa import DSA
from .sha256 import SHA256

class TestCrypto(unittest.TestCase):
    def setUp(self):
        elements = {0, 1, 2, 3}
        addition = lambda a, b: (a + b) % 4
        multiplication = lambda a, b: (a * b) % 4
        self.galois_field = GaloisField(elements, addition, multiplication)
        self.encryption = Encryption(self.galois_field)
        self.decryption = Decryption(self.galois_field)
        self.des = DES()
        self.rsa = RSA()
        self.triple_des_impl = TripleDESImpl()
        self.des_impl = DESImpl()
        self.aes = AES(elements, addition, multiplication)
        self.blowfish = Blowfish(elements, addition, multiplication)
        self.twofish = Twofish(elements, addition, multiplication)
        self.ecc = ECC(elements, addition, multiplication, 1, 1)
        self.dsa = DSA(elements, addition, multiplication, 1, 1, 1)
        self.sha256 = SHA256()

    def test_key_generation(self):
        password = b"password"
        salt = b"salt"
        encryption_key = self.encryption.generate_key(password, salt)
        decryption_key = self.decryption.generate_key(password, salt)
        self.assertIsNotNone(encryption_key)
        self.assertIsNotNone(decryption_key)

    def test_encryption_decryption(self):
        plaintext = "hello"
        password = b"password"
        salt = b"salt"
        key = self.encryption.generate_key(password, salt)
        ciphertext, mac = self.encryption.encrypt(plaintext, key)
        decrypted_text = self.decryption.decrypt(ciphertext, key, mac)
        self.assertEqual(plaintext, decrypted_text)

        # Test edge cases and invalid inputs
        with self.assertRaises(ValueError):
            self.encryption.encrypt(12345, key)  # Invalid plaintext type
        with self.assertRaises(ValueError):
            self.encryption.encrypt(plaintext, "invalid_key")  # Invalid key type
        with self.assertRaises(ValueError):
            self.decryption.decrypt(ciphertext, "invalid_key", mac)  # Invalid key type
        with self.assertRaises(ValueError):
            self.decryption.decrypt("invalid_ciphertext", key, mac)  # Invalid ciphertext type

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

        # Test edge cases and invalid inputs
        with self.assertRaises(ValueError):
            self.encryption.aes.encrypt("invalid_plaintext", key)  # Invalid plaintext type
        with self.assertRaises(ValueError):
            self.encryption.aes.encrypt(plaintext, "invalid_key")  # Invalid key type
        with self.assertRaises(ValueError):
            self.decryption.aes.decrypt(ciphertext, "invalid_key")  # Invalid key type
        with self.assertRaises(ValueError):
            self.decryption.aes.decrypt("invalid_ciphertext", key)  # Invalid ciphertext type

    def test_des_encryption_decryption(self):
        plaintext = "hello"
        key = self.des.generate_key()
        ciphertext = self.des.encrypt(plaintext, key)
        decrypted_text = self.des.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

    def test_rsa_encryption_decryption(self):
        plaintext = "hello"
        private_key, public_key = self.rsa.generate_keys()
        ciphertext = self.rsa.encrypt(plaintext, public_key)
        decrypted_text = self.rsa.decrypt(ciphertext, private_key)
        self.assertEqual(plaintext, decrypted_text)

    def test_triple_des_impl_key_generation(self):
        key = self.triple_des_impl.generate_key(self.triple_des_impl.key_size)
        self.assertEqual(len(key), self.triple_des_impl.key_size)

    def test_triple_des_impl_encryption_decryption(self):
        plaintext = "hello"
        key = self.triple_des_impl.generate_key(self.triple_des_impl.key_size)
        ciphertext = self.triple_des_impl.encrypt(plaintext, key, self.triple_des_impl.block_size)
        decrypted_text = self.triple_des_impl.decrypt(ciphertext, key, self.triple_des_impl.block_size)
        self.assertEqual(plaintext, decrypted_text)

    def test_des_impl_key_generation(self):
        key = self.des_impl.generate_key(self.des_impl.key_size)
        self.assertEqual(len(key), self.des_impl.key_size)

    def test_des_impl_encryption_decryption(self):
        plaintext = "hello"
        key = self.des_impl.generate_key(self.des_impl.key_size)
        ciphertext = self.des_impl.encrypt(plaintext, key, self.des_impl.block_size)
        decrypted_text = self.des_impl.decrypt(ciphertext, key, self.des_impl.block_size)
        self.assertEqual(plaintext, decrypted_text)

    def test_aes_key_expansion(self):
        key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x9f, 0x24, 0x30, 0xc0, 0x8d]
        expanded_key = self.aes.key_expansion(key)
        self.assertEqual(len(expanded_key), 44)  # AES-128 should have 44 words in the expanded key

    def test_aes_encryption_decryption(self):
        plaintext = [0x32, 0x43, 0xf6, 0xa8, 0x88, 0x5a, 0x30, 0x8d, 0x31, 0x31, 0x98, 0xa2, 0xe0, 0x37, 0x07, 0x34]
        key = [0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0xcf, 0x9f, 0x24, 0x30, 0xc0, 0x8d]
        ciphertext = self.aes.encrypt(plaintext, key)
        decrypted_text = self.aes.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

        # Test edge cases and invalid inputs
        with self.assertRaises(ValueError):
            self.aes.encrypt("invalid_plaintext", key)  # Invalid plaintext type
        with self.assertRaises(ValueError):
            self.aes.encrypt(plaintext, "invalid_key")  # Invalid key type
        with self.assertRaises(ValueError):
            self.aes.decrypt(ciphertext, "invalid_key")  # Invalid key type
        with self.assertRaises(ValueError):
            self.aes.decrypt("invalid_ciphertext", key)  # Invalid ciphertext type

    def test_blowfish_key_generation(self):
        key = self.blowfish.generate_key()
        self.assertEqual(len(key), 16)

    def test_blowfish_encryption_decryption(self):
        plaintext = b"hello"
        key = self.blowfish.generate_key()
        ciphertext = self.blowfish.encrypt(plaintext, key)
        decrypted_text = self.blowfish.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

    def test_twofish_key_generation(self):
        key = self.twofish.generate_key()
        self.assertEqual(len(key), 16)

    def test_twofish_encryption_decryption(self):
        plaintext = b"hello"
        key = self.twofish.generate_key()
        ciphertext = self.twofish.encrypt(plaintext, key)
        decrypted_text = self.twofish.decrypt(ciphertext, key)
        self.assertEqual(plaintext, decrypted_text)

    def test_ecc_encryption_decryption(self):
        plaintext = "hello"
        private_key, public_key = self.ecc.generate_keys()
        ciphertext = self.ecc.encrypt(plaintext, public_key)
        decrypted_text = self.ecc.decrypt(ciphertext, private_key)
        self.assertEqual(plaintext, decrypted_text)

    def test_dsa_signing_verification(self):
        message = "hello"
        private_key, public_key = self.dsa.generate_keys()
        signature = self.dsa.sign(message, private_key)
        self.assertTrue(self.dsa.verify(message, signature, public_key))

    def test_sha256_hashing(self):
        message = "hello"
        hash_value = self.sha256.hash(message)
        self.assertIsNotNone(hash_value)

if __name__ == "__main__":
    unittest.main()
