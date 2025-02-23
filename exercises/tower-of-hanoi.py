NUM_DISKS = 3

A = list(range(NUM_DISKS, 0, -1))
B = []
C = []


def move(n, source, auxiliary, target):
    if n <= 0:
        return

    move(n - 1, source, target, auxiliary)

    target.append(source.pop())

    print(A, B, C, '\n')

    move(n - 1, auxiliary, source, target)


move(NUM_DISKS, A, B, C)
