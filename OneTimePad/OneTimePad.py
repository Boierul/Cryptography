import random

# Function that generates a random key stream of a given length
def generate_key_stream(n):
    return bytes([random.randrange(0,256) for i in range(n)])

# Function that XORs strings of bytes
def xor_bytes(key_stream, message):
    length = min(len(key_stream), len(message))
    return bytes([key_stream[i] ^ message[i] for i in range(length)])

# Message to be encrypted
demo_message = 'This is a private message'
# Convert the message to bytes
demo_message = demo_message.encode('utf-8')
# Generate a key stream of the same length as the message
demo_key_stream = generate_key_stream(len(demo_message))
# Encrypt the message
cipher = xor_bytes(demo_key_stream, demo_message)

print('Key stream: ', demo_key_stream)
print('Cipher: ', cipher)
print('Decrypted message: ', xor_bytes(demo_key_stream, cipher))
