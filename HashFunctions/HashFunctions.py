import hashlib

# Function to modify the hash value
def modify(m):
    l = list(m)
    l[0] = l[0] ^ 1
    return bytes(l)

m = "This is the hash value message: ".encode()

sha256 = hashlib.sha256(m)
sha256.update(m)
d = sha256.digest()

print(d)
