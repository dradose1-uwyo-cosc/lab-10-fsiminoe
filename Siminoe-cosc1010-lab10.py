# Forrest Siminoe
# UWYO COSC 1010
# 11/24/24
# Lab 10
# Lab Section: 13

#import modules you will need 

from hashlib import sha256
from pathlib import Path

def generate_hash(password):
    return sha256(password.encode('utf-8')).hexdigest().upper()

def attempt_password_crack():
    hash_path = Path('hash')
    rockyou_path = Path('rockyou.txt')
    
    try:
        target_hash = hash_path.read_text().strip()
    except FileNotFoundError:
        print("The 'hash' file is missing.")
        return
    except Exception as error:
        print(f"Error reading the 'hash' file: {error}")
        return
    
    try:
        with rockyou_path.open('r', encoding='utf-8', errors='ignore') as rockyou_file:
            for password in rockyou_file:
                password = password.strip()
                if generate_hash(password) == target_hash:
                    print(f"Password cracked: {password}")
                    return
    except FileNotFoundError:
        print("The 'rockyou.txt' file is missing.")
    except Exception as error:
        print(f"Error reading the 'rockyou.txt' file: {error}")
    else:
        print("Password not found in the list.")

attempt_password_crack()


# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
