def generateKey(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = {}
    counter = 0
    for c in letters:
        key[c] = letters[(counter + n) % len(letters)]
        counter += 1
    return key

def getDecryptionKey(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher

# Generate the key for the algorithm
key = generateKey(5)
print(key)

# Encrypt the message
message = "BUCATA DE CACAT"
cipher = encrypt(key, message)
print(cipher)

# Decrypt the message by using brute force
for i in range(26):
    dkey = generateKey(i)
    message = encrypt(dkey, cipher)
    print(message)

# Decrypt the message by inserting the known key
    # dkey = getDecryptionKey(key)
    # message = encrypt(dkey, cipher)
    # print(message)
