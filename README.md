# EEE-Intro-to-IOT-SECURITY-LAB-3
Write two separate python programs to demonstrate the basic concept of "Digital Signature".   
Lab 3 – Digital Signatures using RSA in Python

This lab demonstrates how a message can be digitally signed and verified using RSA.

Files:
- client_a.py – This script generates a key pair, signs a message, and saves the message, signature, and public key to files.
- client_b.py – This script loads the saved files and verifies that the message was signed by Client A using the public key.
- message.txt – The original message signed by Client A.
- signature.txt – The digital signature of the message.
- public_key.pem – Client A’s public key used for verification.

Python RSA library used: https://stuvel.eu/python-rsa-doc/

Instructions:
1. Run client_a.py to generate the message and signature.
2. Run client_b.py to verify that the signature is valid.
