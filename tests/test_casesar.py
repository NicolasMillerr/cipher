import cipher
from cipher.caesar import Caesar

machine_1 = Caesar(1)
machine_2 = Caesar(2)

def test_encode():

    assert machine_1.encode("ab") == "BC"
    assert machine_2.encode("oi") == "QK"
    assert machine_1.encode("hello my name is nic") == "IFMMP NZ OBNF JT OJD"
    assert machine_1.encode("hello, my name is nic") == "IFMMP, NZ OBNF JT OJD"

def decode():
    assert machine_1.decode("BC") == "ab"
    assert machine_1.decode("IFMMP NZ OBNF JT OJD") == "hello my name is nic"
