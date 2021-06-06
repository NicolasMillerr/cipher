"""Implements the Caesar class which can encode and decode caesar ciphers"""

class Caesar:
    def __init__(self, key):
        """This should be implemented by future cipher machines. Set the key"""
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.key=key

    def encode(self, plaintext):
        ciphertext = "".join(self._shift(letter, self.key).upper() for letter in plaintext)
        return ciphertext

    def decode(self, ciphertext):
        plaintext = "".join(self._shift(letter, -self.key) for letter in ciphertext.lower())

    def _shift(self, letter, n):
        if letter in self.alphabet:
            return self.alphabet[self._clocksum(self.alphabet.find(letter), n)]
        return letter

    def _clocksum(self, x, n):
        if x + n >= len(self.alphabet):
            return x + n - 26
        return x + n

