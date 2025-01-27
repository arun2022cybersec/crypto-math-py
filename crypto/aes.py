from group_theory.galois_field import GaloisField

class AES(GaloisField):
    """Represents the AES (Advanced Encryption Standard) algorithm using Galois fields."""

    def __init__(self, elements, addition, multiplication):
        """
        Initialize the AES algorithm with elements, addition, and multiplication operations.

        Args:
            elements (set): The set of elements in the Galois field.
            addition (callable): The addition operation for the Galois field.
            multiplication (callable): The multiplication operation for the Galois field.
        """
        super().__init__(elements, addition, multiplication)
        self.Nb = 4  # Number of columns (32-bit words) comprising the State. For AES, Nb = 4.
        self.Nk = 4  # Number of 32-bit words comprising the Cipher Key. For AES-128, Nk = 4.
        self.Nr = 10  # Number of rounds, which is a function of Nk and Nb (which is fixed). For AES-128, Nr = 10.

    def key_expansion(self, key):
        """
        Perform key expansion to generate round keys.

        Args:
            key (list): The cipher key.

        Returns:
            list: The expanded key schedule.
        """
        # Key expansion logic
        def sub_word(word):
            return [self.s_box[b] for b in word]

        def rot_word(word):
            return word[1:] + word[:1]

        w = [0] * (self.Nb * (self.Nr + 1))
        for i in range(self.Nk):
            w[i] = key[4 * i: 4 * (i + 1)]

        for i in range(self.Nk, self.Nb * (self.Nr + 1)):
            temp = w[i - 1]
            if i % self.Nk == 0:
                temp = sub_word(rot_word(temp))
                temp[0] ^= self.rcon[i // self.Nk]
            elif self.Nk > 6 and i % self.Nk == 4:
                temp = sub_word(temp)
            w[i] = [w[i - self.Nk][j] ^ temp[j] for j in range(4)]
        return w

    def encrypt(self, plaintext, key):
        """
        Encrypt the plaintext using the provided key.

        Args:
            plaintext (list): The plaintext to encrypt.
            key (list): The encryption key.

        Returns:
            list: The encrypted ciphertext.
        """
        # Encryption logic
        state = [plaintext[i:i + 4] for i in range(0, len(plaintext), 4)]
        round_keys = self.key_expansion(key)

        def add_round_key(state, round_key):
            return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]

        def sub_bytes(state):
            return [[self.s_box[b] for b in row] for row in state]

        def shift_rows(state):
            return [state[0], state[1][1:] + state[1][:1], state[2][2:] + state[2][:2], state[3][3:] + state[3][:3]]

        def mix_columns(state):
            def mix_single_column(column):
                return [
                    self.galois_mult(column[0], 2) ^ self.galois_mult(column[1], 3) ^ column[2] ^ column[3],
                    column[0] ^ self.galois_mult(column[1], 2) ^ self.galois_mult(column[2], 3) ^ column[3],
                    column[0] ^ column[1] ^ self.galois_mult(column[2], 2) ^ self.galois_mult(column[3], 3),
                    self.galois_mult(column[0], 3) ^ column[1] ^ column[2] ^ self.galois_mult(column[3], 2)
                ]
            return [mix_single_column(col) for col in zip(*state)]

        state = add_round_key(state, round_keys[:self.Nb])
        for round in range(1, self.Nr):
            state = sub_bytes(state)
            state = shift_rows(state)
            state = mix_columns(state)
            state = add_round_key(state, round_keys[round * self.Nb:(round + 1) * self.Nb])
        state = sub_bytes(state)
        state = shift_rows(state)
        state = add_round_key(state, round_keys[self.Nr * self.Nb:])
        return [byte for row in state for byte in row]

    def decrypt(self, ciphertext, key):
        """
        Decrypt the ciphertext using the provided key.

        Args:
            ciphertext (list): The ciphertext to decrypt.
            key (list): The decryption key.

        Returns:
            list: The decrypted plaintext.
        """
        # Decryption logic
        state = [ciphertext[i:i + 4] for i in range(0, len(ciphertext), 4)]
        round_keys = self.key_expansion(key)

        def add_round_key(state, round_key):
            return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]

        def inv_sub_bytes(state):
            return [[self.inv_s_box[b] for b in row] for row in state]

        def inv_shift_rows(state):
            return [state[0], state[1][-1:] + state[1][:-1], state[2][-2:] + state[2][:-2], state[3][-3:] + state[3][:-3]]

        def inv_mix_columns(state):
            def inv_mix_single_column(column):
                return [
                    self.galois_mult(column[0], 14) ^ self.galois_mult(column[1], 11) ^ self.galois_mult(column[2], 13) ^ self.galois_mult(column[3], 9),
                    self.galois_mult(column[0], 9) ^ self.galois_mult(column[1], 14) ^ self.galois_mult(column[2], 11) ^ self.galois_mult(column[3], 13),
                    self.galois_mult(column[0], 13) ^ self.galois_mult(column[1], 9) ^ self.galois_mult(column[2], 14) ^ self.galois_mult(column[3], 11),
                    self.galois_mult(column[0], 11) ^ self.galois_mult(column[1], 13) ^ self.galois_mult(column[2], 9) ^ self.galois_mult(column[3], 14)
                ]
            return [inv_mix_single_column(col) for col in zip(*state)]

        state = add_round_key(state, round_keys[self.Nr * self.Nb:])
        for round in range(self.Nr - 1, 0, -1):
            state = inv_shift_rows(state)
            state = inv_sub_bytes(state)
            state = add_round_key(state, round_keys[round * self.Nb:(round + 1) * self.Nb])
            state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = add_round_key(state, round_keys[:self.Nb])
        return [byte for row in state for byte in row]
