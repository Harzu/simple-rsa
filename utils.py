import base64
import random

def generatePrime(bits = 1024):
    while True:
        p = random.getrandbits(bits)
        if testMilleraRabina(p) == True:
            return p

def testMilleraRabina(prime, rounds = 50):
    if prime == 2 or prime == 3:
        return True

    if prime < 2 or prime % 2 == 0:
        return False

    t = prime - 1
    s = 0
    while t % 2 == 0:
        s += 1
        t //= 2
    
    for _ in range(0, rounds):
        a = random.randint(1, prime - 1)
        x = pow(a, t, prime)

        if x == 1 or x == prime - 1:
            continue

        for _ in range(0, s):
            x = pow(x, 2, prime)
            if x == 1:
                return False
            if x == prime - 1:
                break

        if x != prime - 1:
            return False

    return True

def gcd(a, b):
    while a != 0:
        a, b = b % a, a

    return b

def findModInverse(a, m):
    if gcd(a, m) != 1:
        return None

    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
   
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3

    return u1 % m

