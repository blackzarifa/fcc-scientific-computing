def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return 'Error: Too many problems.'

    splitProblems = [p.split() for p in problems]

    for n1, op, n2 in splitProblems:
        if op not in {'+', '-'}:
            return "Error: Operator must be '+' or '-'."
        if not (n1.isdigit() and n2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        if len(n1) > 4 or len(n2) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    lines = ['', '', '']
    if show_answers:
        lines.append('')

    for n1, op, n2 in splitProblems:
        maxLen = max(len(n1), len(n2)) + 2

        lines[0] += f"{n1:>{maxLen}}    "
        lines[1] += f"{op}{n2:>{maxLen-1}}    "
        lines[2] += f"{'-'*maxLen}    "

        if show_answers:
            int1 = int(n1)
            int2 = int(n2)
            answer = str(int1 + int2 if op == '+' else int1 - int2)
            lines[3] += f'{answer:>{maxLen}}    '

    return '\n'.join(line.rstrip() for line in lines)


def main():
    res = arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

    print(res)


main()
