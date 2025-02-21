NUM_DISKS = 3
NUM_MOVES = 2**NUM_DISKS - 1

rods = {'A': list(range(NUM_DISKS, 0, -1)), 'B': [], 'C': []}


def move(n, source, auxiliary, target):
    print(rods)

    for i in range(NUM_MOVES):
        remainder = (i + 1) % 3
        if remainder == 1:
            print(f'Move {i + 1} allowed between {source} and {target}')
        elif remainder == 2:
            print(f'Move {i + 1} allowed between {source} and {auxiliary}')
        elif remainder == 0:
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')


move(NUM_DISKS, 'A', 'B', 'C')
