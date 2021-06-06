from requests import post

url = "http://localhost:5000/"

def test_encode_endpoint():
    r = post(url+'encode', {
        'key':1,
        'plaintext': 'hello my name is nic'
    })

    assert r.json()['ciphertext'] == "IFMMP NZ OBNF JT OJD"

def test_decode_endpoint():
    r = post(url+'decode', {
        'key':1,
        'ciphertext': 'IFMMP NZ OBNF JT OJD'
    })

    assert r.json()['plaintext'] == "hello my name is nic"
