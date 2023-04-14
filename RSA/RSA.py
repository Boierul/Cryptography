import math
import random


# Function that checks if a number is prime
def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True


# Function that generates a prime number
def get_prime(size):
    while True:
        p = random.randint(size, 2 * size)
        if is_prime(p):
            return p


# Function that computes the least common multiple
def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

# Function that generates a random number e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
def get_e(phi):
    for e in range(2, phi):
        if math.gcd(e, phi) == 1:
            return e
    return False

def get_d(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return False

# Key generation (done by Alice - in private)
#   Step 1: Generate two distinct primes
size = 300
p = get_prime(size)
q = get_prime(size)
print("Generated primes: ", p, q)

#   Step 2: Compute n = p * q
n = p * q
print("Modulus n:", n)

#   Step 3: Compute phi(n) = (p - 1) * (q - 1)
lambda_n = lcm(p-1, q-1)
print("Lambda n (phi):", lambda_n)

#   Step 4: Choose an integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
e = get_e(lambda_n)
print("Public key e:", e)

#   Step 5: Compute the private key d such that d * e = 1 (mod phi(n))
d = get_d(e, lambda_n)
print("Private key d:", d)

print("\n")
print("Done with key generation")
print("Public key: (", e, ",", n, ")")
print("Private key: (", d, ")")

# This is Bob wanting to send a message to Alice
print("\n")
# M is the message
m = 117
c = (m ** e) % n
print("Bob sends:", c)

# Alice decrypts the cipher
m = (c ** d) % n
print("Alice decrypts:", m)