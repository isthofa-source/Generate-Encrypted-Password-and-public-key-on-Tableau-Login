import requests
import json
import binascii
import Crypto
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

tab_server_url = "https://datavisualization.btn.co.id/"

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


# List of passwords
passwords = ["Batara.#@123", "Batara.#@123", "Batara.#@123"]

# Generate encrypted passwords
encrypted_passwords = []
for password in passwords:
    # Generate new public key for each password
    public_key = generate_public_key()
    pk = public_key["keyId"]
    print("Public Key:", pk)
    encrypted_password = asymmetric_encrypt(password, public_key)
    encrypted_passwords.append(encrypted_password)

# Print encrypted passwords
for i, password in enumerate(passwords):
    print(f"Password: {password} \t Encrypted Password: {encrypted_passwords[i]}")
