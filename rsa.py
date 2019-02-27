"""
reference: http://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/
"""

import random


def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def modinv(a, m):
    for x in range(1, m):
        if(a*x) % m == 1:
            return x
    return None


def generate_key(p, q):
    n = p*q
    phi = (p-1)*(q-1)
    e = random.randrange(1, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = modinv(e, phi)

    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    key, n = pk
    cipher = [(ord(char) ** key) % n for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    key, n = pk
    plain = [chr((char ** key) % n)for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    p = 19
    q = 23
    public, private = generate_key(p, q)
    print("public key is ", public, ", private key is ", private)
    message = "test message"
    encrypt_msg = encrypt(private, message)
    print(decrypt(public, encrypt_msg))
