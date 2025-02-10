def verifyCardNumber(number):
    oddSum = sumOddNumbers(number)
    print(oddSum)


def sumOddNumbers(number):
    sum = 0
    oddNumbers = number[::-1][::2]

    for i in oddNumbers:
        sum += int(i)

    return sum


def main():
    cardNumber = '4111-1111-4555-1142'
    translation = str.maketrans({'-': '', ' ': ''})
    translatedNumber = cardNumber.translate(translation)

    verifyCardNumber(translatedNumber)


main()
