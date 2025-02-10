def main():
    cardNumber = '4111-1111-4555-1142'
    translation = str.maketrans({'-': '', ' ': ''})
    translatedNumber = cardNumber.translate(translation)

    print(translatedNumber)


main()
