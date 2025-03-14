def verifyCardNumber(number):
    oddSum = sumOddNumbers(number)
    evenSum = sumEvenNumbers(number)
    total = oddSum + evenSum

    return 0 == total % 10


def sumOddNumbers(number):
    sum = 0
    oddNumbers = number[::-1][::2]

    for i in oddNumbers:
        sum += int(i)

    return sum


def sumEvenNumbers(number):
    sum = 0
    evenNumbers = number[::2]

    for i in evenNumbers:
        double = int(i) * 2
        if double <= 9:
            sum += double
            continue

        firstNum = double // 10
        secondNum = double % 10
        sum += firstNum + secondNum

    return sum


def main():
    cardNumber = '4111-1111-4555-1142'
    translation = str.maketrans({'-': '', ' ': ''})
    translatedNumber = cardNumber.translate(translation)

    isValid = verifyCardNumber(translatedNumber)
    print('Valid!' if isValid else 'Invalid!')


main()
