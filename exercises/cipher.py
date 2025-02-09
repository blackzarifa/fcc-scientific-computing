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


def vigenere(text, key, decrypt=False):
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

        cipherIdx = alphabetIdx + keyIdx * -1 if decrypt else alphabetIdx + keyIdx
        cipher += ALPHABET[cipherIdx % len(ALPHABET)]

    return cipher


text = "Hello Zaira"
key = "python"

print(caesar(text, 3))

vigenereEncryption = vigenere(text, key)
print(vigenereEncryption)
print(vigenere(vigenereEncryption, key, True))
