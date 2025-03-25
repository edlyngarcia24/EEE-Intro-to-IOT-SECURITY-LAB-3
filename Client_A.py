#Guice for Source code: https://stuvel.eu/python-rsa-doc/usage.html#signing-and-verification
#Signing Side

import rsa

# Generate Amy's key pairpy
(amy_pubkey, amy_privkey) = rsa.newkeys(2048) #2048 is the minimum 

# Original message
message = b'Hello, this is Amy. Welcome to Belize!'  # Always in bytes, the b denotes byte literal
# alternative could have been message='text here' .encode ('utf-8')
#Short: always needs to be in byte, python does not read text. 

# Sign the message with Amy’s private key
signature = rsa.sign(message, amy_privkey, 'SHA-256')

# Confirm signing worked
print("Message signed.")

# Save and simulate sending message + signature + public key
with open("message.txt", "wb") as f: # opens the file and wb implies write mode and binary, to write binary data to the file
    f.write(message) #note my file object name is f, could have had any other name

with open("signature.txt", "wb") as f:
    f.write(signature)

with open("public_key.pem", "wb") as f: #stores amy public key in a way that Client B can read it later
    f.write(amy_pubkey.save_pkcs1("PEM")) #PEM: Privacy Enhanced Mail for encoding cryptographic keys

with open("private_key.pem", "wb") as f:
    f.write(amy_privkey.save_pkcs1("PEM")) #Save Private Key for future use, could reuse the same key for future testing or expansion












