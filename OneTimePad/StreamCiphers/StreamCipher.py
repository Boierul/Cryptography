import random

class KeyStream:
    def __init__(self, key=1):
        self.next = key

    #  Pseudo-number generator function
    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2 ** 31
        return self.next
    # Function to get a random byte from the pseudo-number generator
    def get_key_byte(self):
        return self.rand() % 256

# Function to encrypt/decrypt a message (XOR)
def encrypt_decrypt(key, message):
    return bytes([message[i] ^ key.get_key_byte() for i in range(len(message))])

# Function to transmit a message with a given likelihood of error
def transmit(cipher, likelihood):
    b = []
    for c in cipher:
        if random.randrange(0, likelihood) == 0:
            c = c ^ 2 ** random.randrange(0, 8)
        b.append(c)
    return bytes(b)

# key = KeyStream()
# for i in range(10):
#     print(key.get_key_byte())

key = KeyStream(10)
message = 'This is a private message'.encode()
print('Message: ', message)
cipher = encrypt_decrypt(key, message)
print('Cipher', cipher)

cipher = transmit(cipher, 5)

key = KeyStream(10)
message = encrypt_decrypt(key, cipher)
print('Message after decryption: ', message)