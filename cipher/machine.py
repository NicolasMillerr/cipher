import abc

class Machine(abc.ABC):

    def __init__(self, key):
        self.key = key

    @abc.abstractmethod
    def encode(self, plaintext):
        return plaintext

    @abc.abstractmethod
    def decode(self, ciphertext):
        return plaintext
