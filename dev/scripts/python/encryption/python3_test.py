import string
from secrets import choice
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA

cipher_key = ''
password = ''
def gen_key():
    cipher_key = Fernet.generate_key()
    return cipher_key

def test_one():
    alphabet = string.ascii_letters + string.digits
    password = ''.join(choice(alphabet) for i in range(8))
    print(password)

def test_2():
    with open('/usr/share/dict/words') as f:
        words = [word.strip() for word in f]
        password = ''.join(choice(words) for i in range(4))
    return password

def test_3():
    alphabet = string.ascii_letters + string.digits
    while True:
        password = ''.join(choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
        and any(c.isupper() for c in password)
        and sum(c.isdigit() for c in password) >= 3):
            break
    return password

def gen_rsa_pair():
    code = test_3()

    key = RSA.generate(2048, e=65537)
    privatekey = key.exportKey("PEM",passphrase=code, pkcs=8)
    publickey = key.publickey().exportKey("PEM")
    print(code)
    print(privatekey)
    print(publickey)
gen_rsa_pair()
