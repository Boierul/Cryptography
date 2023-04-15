import hashlib

# Suppose we have this public key and private key:
    # Public key -> (e, n): ( 3 , 136627 )
    # Private key -> (d): ( 22647 )

n = 136627
e = 3
d = 22647

# The message that needs to be signed before sending
message = "Bob is cool".encode()

# Step 1: Hash the message
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
# Used modulus n to make sure the hash value is less than n (not used in real-life)
h = int.from_bytes(h, byteorder='big') % n
print("Hash value of message:", h)

# Step 2: Decrypt the hash value (use private key)
sign = (h ** d) % n

# Step 3: Send the message and the signature
print("Message:", message)
print("Signature:", sign)

# Step 4: Verify the signature (use public key)
# Step 4.1: Calculate hash value of the message (used from step 1)
sha256 = hashlib.sha256()
sha256.update(message)
h = sha256.digest()
h = int.from_bytes(h, byteorder='big') % n
print("Hash value of message:", h)

# Step 4.2: Verify the signature
verification = (sign ** e) % n
print("Verification:", verification)

# Step 4.3: Compare the hash value of the message and the verification
if h == verification:
    print("Signature correctly verified")
else:
    print("Signature not correct")
