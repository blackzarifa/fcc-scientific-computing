def merge_sort(array):
    if len(array) <= 1:
        return

    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    left_idx = 0
    right_idx = 0
    sorted_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            array[sorted_idx] = left[left_idx]
            left_idx += 1
        else:
            array[sorted_idx] = right[right_idx]
            right_idx += 1
        sorted_idx += 1

    while left_idx < len(left):
        array[sorted_idx] = left[left_idx]
        left_idx += 1
        sorted_idx += 1

    while right_idx < len(right):
        array[sorted_idx] = right[right_idx]
        right_idx += 1
        sorted_idx += 1


if __name__ == '__main__':
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]
    print('Unsorted array: ')
    print(numbers)

    merge_sort(numbers)
    print('Sorted array: ')
    print(numbers)
