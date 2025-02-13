def main():
    sqrRootBisection(16)


def sqrRootBisection(target, tolerance=1e-7, maxIterations=100):
    if target < 0:
        raise ValueError(
            'Square root of negative number is not defined in real numbers'
        )

    if target == 0 or target == 1:
        print(f'The square root of {target} is {target}')
        return target

    low = 0
    high = target
    root = None

    for _ in range(maxIterations):
        mid = (high + low) / 2
        squareMid = mid**2

        if abs(squareMid - target) < tolerance:
            root = mid
            break

        if squareMid < target:
            low = mid
        else:
            high = mid

    if root is None:
        print(f"Failed to converge within {maxIterations} iterations.")
    else:
        print(f'The square root of {target} is approximately {root}')

    return root


main()
