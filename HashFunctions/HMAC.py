import hashlib

def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

# Alice and Bob share a secret key
secret_key = "secret key".encode()

# Alice wants to compute a MAC for a message
m = "Bob you are 1.5m".encode()
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac = sha256.digest()
print("Message:", m, "HMAC:", hmac)

# Eve comes along and modifies the message
m = modify(m)
print("Message (modified by Eve):", m)

# Bob receives the message and the MAC
sha256 = hashlib.sha256()
sha256.update(secret_key)
sha256.update(m)
hmac2 = sha256.digest()
print("Message:", m, "HMAC:", hmac)
