# Generate-Encrypted-Password-and-public-key-on-Tableau-Login
This script is useful for creating a list of encrypted passwords that are useful for the bruteforce login process on Tableau

:warning: **DISCLAIMER**: This script is only used for someone who has been validated to do so. Apart from that, the manufacturer is not responsible. Thank You

## Description
Here I created a script using Python 3 where the script's function is only to get **encryptedPassword** and **keyId**. Where the two parameters function to perform the login process on a **Tableau application**. To carry out the brute force process, you can use tools such as **Bupsuite (intruder)**. I am attaching 2 scripts in this script where the **standard script** is only for generating 1 encrypted password and keyId (Publickey) and a **script file** for generating encrypted passwords along with keyID (Publickey) in a specified file.

## POC (Proof-Of-Concept)
### Standard Script
Run the script with command:
```py
python GenerateEncryptPassword-Tableau.py
```
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/488929bf-fbf9-40ff-8f92-1f6459ab1541)
![image](https://github.com/isthofa-source/Generate-Encrypted-Password-and-public-key-on-Tableau-Login/assets/75401288/dcb9217a-ee18-4267-8a6e-66d0e428052d)

### Script File
Run the script with command:
```py
python GenerateListEncryptedAndKeyLogin-File-Tableau.py
```
