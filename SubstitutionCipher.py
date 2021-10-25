import random

def generateKey():
    letters = "ABCDEFGHIJJKLMNOPQRSTUVWXYZ"
    cletters = list(letters)
    key = {}
    for c in letters:
        key[c] = cletters.pop(random.randint(0, len(cletters) - 1))
    return key

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

def getDecryptKey(key):
    dkey = {}
    for k in key:
        dkey[key[k]] = k
    return dkey


# Generate the key for the algorithm
key = generateKey()
print(key)

# Encrypt the message
message = "BLEA BUDU"
cipher = encrypt(key, message)
print(cipher)

# Decrypt the message by using the known key
dkey = getDecryptKey(key)
message = encrypt(dkey, cipher)
print(message)