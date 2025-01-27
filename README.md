# CryptoMathPy

CryptoMathPy is a Python project that explores the intersection of cryptography, mathematics, and Python programming. It begins with fundamental mathematical concepts such as set theory, relations, and functions, and gradually progresses to advanced topics like group theory and Galois fields. The project culminates in the implementation of various encryption and decryption algorithms, demonstrating practical applications of cryptographic techniques in Python.

## Features

- **Mathematical Foundations**: Implement mathematical concepts of sets, relations, functions, group theory, rings, fields, and Galois fields in Python.
- **Encryption Algorithms**: Develop encryption algorithms including AES, RSA, and others.
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
key = encryption.generate_key()

# Encrypt and decrypt a message
plaintext = "hello"
ciphertext = encryption.encrypt(plaintext, key)
decrypted_text = decryption.decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")
```

## Contributing

Contributions to CryptoMathPy are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and ensure that the code passes all tests.
4. Submit a pull request with a clear description of your changes.

## License

This project is licensed under the [MIT License](LICENSE).

