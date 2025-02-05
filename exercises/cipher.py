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


text = "Hello World"
print(caesar(text, 3))
