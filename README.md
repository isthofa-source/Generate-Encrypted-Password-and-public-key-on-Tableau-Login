# Generate-Encrypted-Password-and-public-key-on-Tableau-Login
This script is useful for creating a list of encrypted passwords that are useful for the bruteforce login process on Tableau

:warning: **DISCLAIMER**: This script is only used for someone who has been validated to do so. Apart from that, the manufacturer is not responsible. Thank You

## POC (Proof-Of-Concept)
### Standard Script
Run the script with command:
```py
python GenerateEncryptPassword-Tableau.py
```
Enter the desired target URL and password. Then you will get an encrypted PublicKey and Password
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/488929bf-fbf9-40ff-8f92-1f6459ab1541)
Next try to log in (Via Repeater). And it looks like a successful login with response code 200
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/33ce86b8-3c65-44ad-8f35-03ef94acf3c6)


### Script File
Run the script with command:
```py
python GenerateListEncryptedAndKeyLogin-File-Tableau.py
```
Enter the desired URL and location of the password list file that has been provided. It is recommended to put the location of the password list file in the same folder as the script. And the results of the encrypted password and Public key can be accessed in a separate file according to that name. The generate process is obtained per line so it can be copied and pasted on brute-force tools such as Intruder (Burpsuite).
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/95dc945b-fb97-4caa-adc1-055766c3777e)
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/35f6fdf2-67e2-46f0-a84a-d71f8e958005)

## Requirements
Please note that this script assumes you have installed the **requests**, **json**, **binascii**, **Crypto**, and **base64** libraries. If it's not already installed, you can install it using the command :
```py
pip install [library_name]
```
## Description
Here I created a script using Python 3 where the script's function is only to get **encryptedPassword** and **keyId**. Where the two parameters function to perform the login process on a **Tableau application**. To carry out the brute force process, you can use tools such as **Bupsuite (intruder)**. I am attaching 2 scripts in this script where the **standard script** is only for generating 1 encrypted password and keyId (Publickey) and a **script file** for generating encrypted passwords along with keyID (Publickey) in a specified file.
To get the encrypted password along with the private key, we have to do the following steps:
- Generate a **Public Key (keyId)** which we can use to encrypt our password which will be used for the login process
- Encrypt user passwords with PKCS1 RSA encryption

Where in the process of getting the public key we need the parameter values of the following:
- The keyId
- The modulus “n”
- The exponent “e”
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/fac50239-d643-4fb1-8555-92de5f61cfb8)

Make it, that's it. Hope it is useful. Thank You :)
