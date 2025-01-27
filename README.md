# CryptoMathPy

CryptoMathPy is a Python project that explores the intersection of cryptography, mathematics, and Python programming. It begins with fundamental mathematical concepts such as set theory, relations, and functions, and gradually progresses to advanced topics like group theory and Galois fields. The project culminates in the implementation of various encryption and decryption algorithms, demonstrating practical applications of cryptographic techniques in Python.

## Features

- **Mathematical Foundations**: Implement mathematical concepts of sets, relations, functions, group theory, rings, fields, and Galois fields in Python.
- **Encryption Algorithms**: Develop encryption algorithms including AES, RSA, DES, 3DES, Blowfish, Twofish, and others.
- **Decryption Algorithms**: Implement corresponding decryption algorithms for encrypted data.
- **Python Applications**: Create Python applications for encryption, decryption, and data security.
- **Documentation and Examples**: Provide comprehensive documentation and usage examples for each implemented concept and algorithm.

## Installation

To use CryptoMathPy, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/CryptoMathPy.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Explore the project directories and run the Python scripts to explore various mathematical concepts and cryptographic algorithms.

## Usage

- **Mathematical Concepts**: Explore mathematical concepts by running scripts in the `SetTheory`, `GroupTheory`, `RingTheory`, `FieldTheory`, and `GaloisFields` directories.
- **Encryption and Decryption**: Use the scripts in the `EncryptionAlgorithms` and `DecryptionAlgorithms` directories to encrypt and decrypt data using different algorithms.
- **Python Applications**: Run the Python applications in the `Applications` directory for practical demonstrations of cryptographic techniques.

## Examples

### Ring Class

The `Ring` class represents a mathematical ring, inheriting from the `Group` class. It includes addition and multiplication operations and ensures the distributive property.

```python
from group_theory.ring_theory import Ring

# Define addition and multiplication operations
def addition(a, b):
    return (a + b) % 5

def multiplication(a, b):
    return (a * b) % 5

# Create a ring with elements {0, 1, 2, 3, 4}
ring = Ring({0, 1, 2, 3, 4}, addition, multiplication)

# Check if it forms a ring
print(ring.is_ring())  # Output: True
```

### Field Class

The `Field` class represents a mathematical field, inheriting from the `Ring` class. It includes multiplicative inverses for non-zero elements and ensures field properties.

```python
from group_theory.field_theory import Field

# Define addition and multiplication operations
def addition(a, b):
    return (a + b) % 7

def multiplication(a, b):
    return (a * b) % 7

# Create a field with elements {0, 1, 2, 3, 4, 5, 6}
field = Field({0, 1, 2, 3, 4, 5, 6}, addition, multiplication)

# Check if it forms a field
print(field.is_field())  # Output: True
```

### Galois Field Class

The `GaloisField` class represents a Galois field (finite field), inheriting from the `Field` class. It includes finite field arithmetic and ensures Galois field properties.

```python
from group_theory.galois_field import GaloisField

# Define addition and multiplication operations
def addition(a, b):
    return (a + b) % 3

def multiplication(a, b):
    return (a * b) % 3

# Create a Galois field with elements {0, 1, 2}
galois_field = GaloisField({0, 1, 2}, addition, multiplication)

# Check if it forms a Galois field
print(galois_field.is_galois_field())  # Output: True
```

### Encryption and Decryption

The `Encryption` and `Decryption` classes represent encryption and decryption algorithms using Galois fields.

```python
from crypto.encryption import Encryption
from crypto.decryption import Decryption
from group_theory.galois_field import GaloisField

# Define addition and multiplication operations
def addition(a, b):
    return (a + b) % 3

def multiplication(a, b):
    return (a * b) % 3

# Create a Galois field with elements {0, 1, 2}
galois_field = GaloisField({0, 1, 2}, addition, multiplication)

# Initialize encryption and decryption with the Galois field
encryption = Encryption(galois_field)
decryption = Decryption(galois_field)

# Generate a key
password = b"my_password"
salt = b"my_salt"
key = encryption.generate_key(password, salt)

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext, mac = encryption.encrypt(plaintext, key)
decrypted_text = decryption.decrypt(ciphertext, key, mac)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### DES Algorithm

The `DES` class represents the Data Encryption Standard algorithm with encryption and decryption methods.

```python
from crypto.des import DES

# Initialize DES
des = DES()

# Generate a key
key = des.generate_key()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = des.encrypt(plaintext, key)
decrypted_text = des.decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### RSA Algorithm

The `RSA` class represents the Rivest-Shamir-Adleman algorithm with key generation, encryption, and decryption methods.

```python
from crypto.rsa import RSA

# Initialize RSA
rsa = RSA()

# Generate keys
private_key, public_key = rsa.generate_keys()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = rsa.encrypt(plaintext, public_key)
decrypted_text = rsa.decrypt(ciphertext, private_key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### 3DES Algorithm

The `TripleDES` class represents the Triple Data Encryption Standard algorithm with encryption and decryption methods.

```python
from crypto.triple_des import TripleDES

# Initialize 3DES
triple_des = TripleDES()

# Generate a key
key = triple_des.generate_key()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = triple_des.encrypt(plaintext, key)
decrypted_text = triple_des.decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### Blowfish Algorithm

The `Blowfish` class represents the Blowfish algorithm with encryption and decryption methods.

```python
from crypto.blowfish import Blowfish

# Initialize Blowfish
blowfish = Blowfish()

# Generate a key
key = blowfish.generate_key()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = blowfish.encrypt(plaintext, key)
decrypted_text = blowfish.decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### Twofish Algorithm

The `Twofish` class represents the Twofish algorithm with encryption and decryption methods.

```python
from crypto.twofish import Twofish

# Initialize Twofish
twofish = Twofish()

# Generate a key
key = twofish.generate_key()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = twofish.encrypt(plaintext, key)
decrypted_text = twofish.decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### ECC Algorithm

The `ECC` class represents the Elliptic Curve Cryptography algorithm with key generation, encryption, and decryption methods.

```python
from crypto.ecc import ECC

# Initialize ECC
ecc = ECC()

# Generate keys
private_key, public_key = ecc.generate_keys()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = ecc.encrypt(plaintext, public_key)
decrypted_text = ecc.decrypt(ciphertext, private_key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

### DSA Algorithm

The `DSA` class represents the Digital Signature Algorithm with key generation, signing, and verification methods.

```python
from crypto.dsa import DSA

# Initialize DSA
dsa = DSA()

# Generate keys
private_key, public_key = dsa.generate_keys()

# Sign and verify a message
message = "hello"
signature = dsa.sign(message, private_key)
is_valid = dsa.verify(message, signature, public_key)

print(f"Message: {message}")
print(f"Signature: {signature}")
print(f"Is Valid: {is_valid}")
```

### SHA-256 Algorithm

The `SHA256` class represents the Secure Hash Algorithm 256-bit with methods for hashing data.

```python
from crypto.sha256 import SHA256

# Initialize SHA-256
sha256 = SHA256()

# Hash a message
message = "hello"
hash_value = sha256.hash(message)

print(f"Message: {message}")
print(f"Hash Value: {hash_value}")
```

## Security Practices and Guidelines

### Secure Key Generation

- Use a secure random number generator for key generation to ensure the keys are unpredictable.
- Avoid using hardcoded keys or weak key generation methods.

### Input Validation and Error Handling

- Validate all inputs to encryption and decryption methods to prevent invalid data from causing errors or vulnerabilities.
- Implement proper error handling to manage exceptions and errors gracefully.

### Secure Key Storage and Management

- Store keys securely and avoid exposing them in plaintext.
- Use secure key management practices to protect keys from unauthorized access.

### Secure Data Handling

- Securely handle and erase sensitive data like keys and plaintext from memory to prevent data leakage.
- Use secure coding practices to protect sensitive data throughout the encryption and decryption processes.

### Testing and Validation

- Test encryption and decryption methods for edge cases and invalid inputs to ensure robustness and security.
- Regularly review and update the code to address potential security vulnerabilities.

## Contributing

Contributions to CryptoMathPy are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code passes all tests.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

