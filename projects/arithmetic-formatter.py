def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    splitProblems = []
    for p in problems:
        splitProblems.append(p.split(' '))

    for p in splitProblems:
        if p[1] != '+' or p[1] != '-':
            print("Error: Operator must be '+' or '-'.")
            break
        if not p[0].isdigit() or not p[2].isdigit():
            print('Error: Numbers must only contain digits.')
            break
        if len(p[0]) > 4 or len(p[2]) > 4:
            print('Error: Numbers cannot be more than four digits.')
            break


def main():
    arithmetic_arranger(["32a + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)


main()
