
def quickSort(numbers):

    print("Sorting:", numbers)

    if len(numbers) == 1:
        return [numbers[0]]

    if (len(numbers) == 2):
        if (numbers[1] < numbers[0]):
            return [numbers[1], numbers[0]]
        return numbers

    pivot = numbers[0]
    left = []
    right = []

    print("Pivot:", pivot)

    for number in numbers[1:]:
        if number < pivot:
            left.append(number)
        else:
            right.append(number)

    sorted = quickSort(left) + [pivot] + quickSort(right)
    print("Sorted:", sorted)
    print("-------------------")
    return sorted

numbers = [170, 45, 75, 90, 802, 24, 2, 66]

print(quickSort(numbers))

