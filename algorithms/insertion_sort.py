def insertion_sort(list_to_sort, pointer=1):
    if pointer < len(list_to_sort):
        val = list_to_sort.pop(pointer)
        sorted_part = list_to_sort[:pointer]
        for i in range(len(sorted_part)):
            if list_to_sort[i] >= val:
                list_to_sort.insert(i, val)
                break
            if i == len(sorted_part) - 1:
                list_to_sort.insert(i + 1, val)
        insertion_sort(list_to_sort, pointer + 1)


if __name__ == "__main__":
    arrays = [
        [11, 3, 2, 15, 45, 34, 12, 98, 44],
        [1, 3, 5, 7, 8, 12, 45, 12, 66],
        [8, 5, 4, 2, 1],
        [],
        [2],
        ['New York', 'Paris', 'Warsaw', 'Vilnius', 'Madrid']
    ]
    for array in arrays:
        insertion_sort(array)
        print(array)
