import hashlib
import hmac

def pbkdf2_hmac(hash_name, password, salt, iterations, dklen=None):
    """
    Implement the PBKDF2 key derivation function with HMAC as the pseudorandom function.

    Args:
        hash_name (str): The name of the hash function to use (e.g., 'sha256').
        password (bytes): The password to derive the key from.
        salt (bytes): The salt to use in the key derivation.
        iterations (int): The number of iterations to perform.
        dklen (int, optional): The length of the derived key. If None, the length of the hash function output is used.

    Returns:
        bytes: The derived key.
    """
    if not isinstance(password, bytes):
        raise TypeError("Password must be a byte string")
    if not isinstance(salt, bytes):
        raise TypeError("Salt must be a byte string")
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("Iterations must be a positive integer")
    if dklen is not None and (not isinstance(dklen, int) or dklen <= 0):
        raise ValueError("dklen must be a positive integer or None")

    hash_func = hashlib.new(hash_name)
    hlen = hash_func.digest_size
    if dklen is None:
        dklen = hlen

    if dklen > (2**32 - 1) * hlen:
        raise OverflowError("dklen too large")

    def F(P, S, c, i):
        U = hmac.new(P, S + i.to_bytes(4, 'big'), hash_name).digest()
        result = bytearray(U)
        for _ in range(1, c):
            U = hmac.new(P, U, hash_name).digest()
            result = bytearray(x ^ y for x, y in zip(result, U))
        return bytes(result)

    l = -(-dklen // hlen)
    r = dklen - (l - 1) * hlen

    derived_key = b''.join(F(password, salt, iterations, i + 1) for i in range(l))
    return derived_key[:dklen]
