import secrets
import string
import re


def generate_password(length, nums, special_chars, uppercase, lowercase):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    while True:
        pw = ''
        for _ in range(length):
            pw += secrets.choice(all_chars)

        constraints = [
            (nums, r'\d'),
            (lowercase, r'[a-z]'),
            (uppercase, r'[A-Z]'),
            (special_chars, fr'[{symbols}]'),
        ]

        if all(
            constraint <= len(re.findall(pattern, pw))
            for constraint, pattern in constraints
        ):
            break

    return pw


def main():
    pw = generate_password(8, 1, 1, 1, 1)
    print(pw)


main()
