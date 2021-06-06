import cipher
from cipher.caesar import shift, encode, decode

def test_shift():
    assert shift("a", 1) == "b"
    assert shift("z", 1) == "a"

def test_encode():
    assert encode("ab", 1) == "BC"
    assert encode("oi", 2) == "QK"
    assert encode("hello my name is nic", 1) == "IFMMP NZ OBNF JT OJD"
    assert encode("hello, my name is nic", 1) == "IFMMP, NZ OBNF JT OJD"

def decode():
    assert decode("BC", 1) == "ab"
    assert decode("IFMMP NZ OBNF JT OJD", 1) == "hello my name is nic"
