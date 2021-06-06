alphabet = "abcdefghijklmnopqrstuvwxyz"
from .machine import Machine


class CaesarMachine(Machine):
    def __init__(self, key):
        super().__init__(key)

def clocksum(x, n):
    if x + n > 25:
        return x + n - 26
    return x + n


def shift(letter, n):
    if letter in alphabet:
        return alphabet[clocksum(alphabet.find(letter), n)]
    return letter


def encode(plaintext, order):

    return "".join(shift(letter, order).upper() for letter in plaintext)


def decode(ciphertext, order):

    return "".join(shift(letter, -order) for letter in ciphertext.lower())


def main():
    print(len(alphabet))


if __name__ == "__main__":
    main()
