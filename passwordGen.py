import random

def generatePassword(size):
    password = ''
    for s in range(0,size):
        password += chr(random.randint(33,126))
    return password

passwords = []
amount = input("How many passwords to generate?")
for i in range(0,int(amount)):
    size = input("What size should the password be?")
    passwords.append(generatePassword(int(size)))

for s in passwords:
    print(s)
