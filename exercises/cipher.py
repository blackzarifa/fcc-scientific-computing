text = "Hello Worldxyz"
shift = 3


def caesar(text, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = ""

    for i in text:
        charIdx = alphabet.find(i.lower())
        if charIdx == -1:
            cipher += i

        newIdx = (charIdx + shift) % len(alphabet)
        cipher += alphabet[newIdx]

    return cipher


print(caesar(text, shift))
