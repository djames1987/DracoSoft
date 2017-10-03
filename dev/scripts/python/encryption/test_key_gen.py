from Crypto.PublicKey import RSA
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

secret_code = "Unguessable"

def gen_rsa_key():
    key = RSA.generate(2048)
    encryption_key = key.exportKey(passphrase=secret_code, pkcs=8, protection="scryptAndAES128-CBC")

    file_out = open("rsa_key.bin", "wb")
    file_out.write(encryption_key)
    file_out.close()

    print(key.publickey().exportKey())

def read_rsa_key():
    encode_key = open("rsa_key.bin", "rb").read()
    key = RSA.import_key(encode_key, passphrase=secret_code)
    print(key.publickey().exportKey())
