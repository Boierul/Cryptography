class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return (self.rand()//2**23) % 256

# Function that encrypts a message
def encrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

# Function that brute forces the key
def brute_force(plain, cipher):
        for k in range(2 ** 31):
            bf_key = KeyStream(k)
            for i in range(len(plain)):
                xor_value = plain[i] ^ cipher[i]
                if xor_value != bf_key.get_key_byte():
                    break
            else:
                return k
        return False

# Or use this for brute force
def brute_force_alternative(plaintext, ciphertext):
    # insert code here
    for seed in range(2**31):
        key = KeyStream(seed)
        decrypted = encrypt(key, ciphertext)
        if decrypted.startswith(plaintext):
            return seed

    return None

# This is Alice
secret_key = 34567
print(secret_key)
key = KeyStream(secret_key)
header = "MESSAGE: "
message = header + "My secret message to Bob"
message = message.encode()
cipher = encrypt(key, message)

# This is Bob
key = KeyStream(secret_key)
message = encrypt(key, cipher)
print(message)

# This is Eve
bf_key = brute_force(header.encode(), cipher)
print("Eve's brute force key:", bf_key)
key = KeyStream(bf_key)
message = encrypt(key, cipher)
print(message)
