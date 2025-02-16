import secrets
import string
import re


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
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


if __name__ == '__main__':
    pw = generate_password(length=8)
    print(pw)
