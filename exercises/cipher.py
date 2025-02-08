ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, shift):
    cipher = ""

    for i in text:
        charIdx = ALPHABET.index(i.lower())
        if charIdx == -1:
            cipher += i

        newIdx = (charIdx + shift) % len(ALPHABET)
        cipher += ALPHABET[newIdx]

    return cipher


text = "Hello World"
print(caesar(text, 3))
