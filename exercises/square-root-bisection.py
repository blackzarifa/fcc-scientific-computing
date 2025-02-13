def sqrRootBisection(target, tolerance=1e-7, maxIterations=100):
    if target < 0:
        raise ValueError(
            'Square root of negative number is not defined in real numbers'
        )

    if target == 0 or target == 1:
        print(f'The square root of {target} is {target}')
        return target

    low = 0
    high = max(1, target)
    root = None

    for _ in range(maxIterations):
        pass
