def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    splitProblems = []
    for p in problems:
        splitProblems.append(p.split(' '))

    firstLine = ''
    secondLine = ''
    dashLine = ''
    answerLine = ''

    for p in splitProblems:
        len1 = len(p[0])
        len2 = len(p[2])

        if p[1] != '+' and p[1] != '-':
            print("Error: Operator must be '+' or '-'.")
            break
        if not p[0].isdigit() or not p[2].isdigit():
            print('Error: Numbers must only contain digits.')
            break
        if len1 > 4 or len2 > 4:
            print('Error: Numbers cannot be more than four digits.')
            break

        maxLen = max(len1, len2) + 2

        for _ in range(maxLen - len1):
            firstLine += ' '
        for _ in range(maxLen - len2):
            secondLine += ' '

        firstLine += p[0]
        secondLine += p[2]

        for _ in range(maxLen):
            dashLine += '-'

        firstLine += '    '
        secondLine += '    '
        dashLine += '    '
        answerLine += '    '
        print(firstLine)
        print(secondLine)
        print(dashLine)


def main():
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)


main()
