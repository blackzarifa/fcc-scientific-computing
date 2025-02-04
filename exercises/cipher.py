text = "Hello Worldxyz"
shift = 3


def caesar(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""

    for i in text:
        charIdx = alphabet.find(i.lower())
        if charIdx == -1:
            cipher += i

        if charIdx >= len(alphabet) - shift:
            charIdx -= len(alphabet)

        cipherChar = alphabet[charIdx + shift]
        cipher += cipherChar

    return cipher


print(caesar(text, shift))
