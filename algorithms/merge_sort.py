def merge_sorted_lists(list_1, list_2, list_to_sort):
    len_1 = len(list_1)
    len_2 = len(list_2)

    pointer_1 = pointer_2 = pointer_orig = 0

    while pointer_1 < len_1 and pointer_2 < len_2:
        if list_1[pointer_1] <= list_2[pointer_2]:
            list_to_sort[pointer_orig] = list_1[pointer_1]
            pointer_1 += 1
        else:
            list_to_sort[pointer_orig] = list_2[pointer_2]
            pointer_2 += 1
        pointer_orig += 1

    while pointer_1 < len_1:
        list_to_sort[pointer_orig] = list_1[pointer_1]
        pointer_1 += 1
        pointer_orig += 1

    while pointer_2 < len_2:
        list_to_sort[pointer_orig] = list_2[pointer_2]
        pointer_2 += 1
        pointer_orig += 1


def merge_sort(list_to_sort):
    if len(list_to_sort) <= 1:
        return list_to_sort

    mid = len(list_to_sort) // 2
    left = list_to_sort[:mid]
    right = list_to_sort[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_lists(left, right, list_to_sort)


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
        merge_sort(array)
        print(array)
