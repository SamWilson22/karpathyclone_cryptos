import hashlib
import cryptos as sam_okay_cryptos 

def test_sha256():

    test_bytes = [
        b'',
        b'abc', # as seen in NIST docs
        b'hello',
        b'a longer message to make sure that a larger number of blocks works okay too'*15
    ]

    for b in test_bytes:
        print(b)
        gt = hashlib.sha256(b).hexdigest()
        yolo = sam_okay_cryptos.sha256(b).hex()
        assert gt == yolo