password = input ("Enter a password: ")

is_secure = True

#Lenght check
if len (password) < 12:
    print ("Password is too short (minimum 12 characters)")
    print ("\nFinal result:")
    print ("Password is NOT secure")
    exit ()
print ("Password lenght is OK")
# Wordlist check (local common passwords)
try:
    with open("common_passwords.txt", "r") as file:
        for line in file:
            if password == line.strip():
                print("Password found in common password list")
                is_secure = False
except FileNotFoundError:
    print("Wordlist file not found, skipping wordlist check")


#Number check 
has_number = False

for character in password:
    if character.isdigit ():
        has_number = True

if not has_number:
    print ("Password must contain at least one number")
    is_secure = False
else:
    print ("Password contains a number")

# Uppercase letter check
has_uppercase = False

for character in password:
    if character.isupper():
        has_uppercase = True

if not has_uppercase:
    print ("Password must contain at least one uppercase")
    is_secure = False
else:
    print ("Password contains an uppercase letter") 

#Special character check
special_characters = "!@#$%^&*()-_=+[]{};:,.<>?/"
has_special = False

for character in password:
    if character in special_characters:
        has_special = True

if not has_special:
    print ("Password must contain at least one special character")
    is_secure = False
else:
    print ("Password contains a special character")  

#Final result
print("\nFinal result:")
if is_secure:
    print ("Password is secure")
else: print ("Password is NOT secure")

