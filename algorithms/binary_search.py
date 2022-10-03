def binary_search(number_to_search, list_of_numbers):
    left = 0
    right = len(list_of_numbers) - 1
    pos = (left + right) // 2
    while right >= left:
        cur_number = list_of_numbers[pos]
        if cur_number == number_to_search:
            return pos
        elif cur_number > number_to_search:
            right = pos - 1
        elif cur_number < number_to_search:
            left = pos + 1
        pos = (left + right) // 2
    raise Exception(f'No such number {number_to_search} in the list of numbers')


def binary_search_rec(number_to_search, list_of_numbers, left=0, right=None):
    right = len(list_of_numbers) - 1 if right is None else right
    if right < left:
        raise Exception(f'No such number {number_to_search} in the list of numbers')
    pos = (left + right) // 2
    cur_number = list_of_numbers[pos]
    if cur_number == number_to_search:
        return pos
    elif cur_number > number_to_search:
        right = pos - 1
    elif cur_number < number_to_search:
        left = pos + 1
    return binary_search_rec(number_to_search, list_of_numbers, left, right)


if __name__ == '__main__':
    numbers = [1, 5, 8, 12, 15, 20, 25, 45, 50, 67, 68, 69, 86, 88, 89, 100, 102, 104, 108]
    number_to_find = 86
    # position = binary_search(number_to_find, numbers)
    position = binary_search_rec(number_to_find, numbers)
    print(position)
