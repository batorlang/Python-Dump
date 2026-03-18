#Task two
import random
import string
LETTERS = string.ascii_letters
DIGITS = string.digits
SPECIAL = string.punctuation
COMB = LETTERS + DIGITS + SPECIAL
random.seed(8292)
def generate_password(length):
    password = ''.join(random.choice(COMB) for _ in range(length))
    return password

length = input("Enter the length of the password:\n")

while not length.isdigit() or int(length) <= 0:
    print("Password length must be a positive integer.")
    length = input("Enter the length of the password:\n")

length = int(length)

password = generate_password(length)
print(f"Generated password: {password}")
