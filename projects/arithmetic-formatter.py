def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    splitProblems = []
    for p in problems:
        splitProblems.append(p.split(' '))

    print(splitProblems)


def main():
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)


main()
