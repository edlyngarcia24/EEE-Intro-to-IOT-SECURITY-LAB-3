import rsa

# Step 1: Load the public key
with open("public_key.pem", "rb") as f: #rb: open adn read it in binary
    amy_pubkey = rsa.PublicKey.load_pkcs1(f.read())

# Step 2: Load the message
with open("message.txt", "rb") as f:
    message = f.read()

# Step 3: Load the signature
with open("signature.txt", "rb") as f:
    signature = f.read()

# Step 4: Verify the signature
try: #Try and except is purely python and is used for handling errors to avoid a crash in program.
    rsa.verify(message, signature, amy_pubkey)
    print("Signature verified. Message is authentic.")
except rsa.VerificationError:
    print("Signature verification failed. Message may be tampered with.")

#alternative way to check was 
#rsa.verify(message, signature, pub_key)
#print("Verified!")
