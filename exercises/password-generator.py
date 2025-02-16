import secrets
import string


def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    all_chars = letters + digits + symbols

    pw = ''
    for _ in range(length):
        pw += secrets.choice(all_chars)

    return pw


def main():
    pw = generate_password(8)
    print(pw)


main()
