ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def caesar(text, shift):
    cipher = ""

    for i in text:
        charIdx = ALPHABET.find(i.lower())
        if charIdx == -1:
            cipher += i
            continue

        newIdx = (charIdx + shift) % len(ALPHABET)
        cipher += ALPHABET[newIdx]

    return cipher


def vigenere(text, key):
    cipher = ""
    text = text.lower()
    key = key.lower()

    for i in range(len(text)):
        char = text[i]
        alphabetIdx = ALPHABET.find(char)
        if alphabetIdx == -1:
            cipher += char
            continue

        keyChar = key[i % len(key)]
        keyIdx = ALPHABET.index(keyChar)

        cipher += ALPHABET[(alphabetIdx + keyIdx) % len(ALPHABET)]

    return cipher


text = "Hello World"
print(caesar(text, 3))
print(vigenere(text, "python"))
