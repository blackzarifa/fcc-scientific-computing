def main():
    print(convertToSnakeCase('aLongAndComplexString'))


# Converts a Pascal or Camel cased string
def convertToSnakeCase(string):
    snakeCasedList = []
    for char in string:
        newChar = f'_{char.lower()}' if char.isupper() else char
        snakeCasedList.append(newChar)

    return ''.join(snakeCasedList).strip('_')


main()
