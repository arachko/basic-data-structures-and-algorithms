def swap_elements(index_1, index_2, list_):
    tmp = list_[index_1]
    list_[index_1] = list_[index_2]
    list_[index_2] = tmp


def partition(list_to_sort, start=None, end=None):
    pivot_index = start
    pivot = list_to_sort[pivot_index]

    while start < end:
        while start < len(list_to_sort) and list_to_sort[start] <= pivot:
            start += 1

        while list_to_sort[end] > pivot:
            end -= 1

        if start < end:
            swap_elements(start, end, list_to_sort)

    swap_elements(pivot_index, end, list_to_sort)

    return end


def quick_sort(list_to_sort, start=0, end=None):
    if end is None:
        end = len(list_to_sort) - 1
    if start < end:
        partition_index = partition(list_to_sort, start, end)
        quick_sort(list_to_sort, start, partition_index - 1)
        quick_sort(list_to_sort, partition_index + 1, end)


if __name__ == "__main__":
    arrays = [
        [11, 3, 2, 15, 45, 34, 12, 98, 44],
        [1, 3, 5, 7, 8, 12, 45, 66],
        [8, 5, 4, 2, 1],
        [],
        [2],
        ['New York', 'Paris', 'Warsaw', 'Vilnius', 'Madrid']
    ]
    for array in arrays:
        quick_sort(array)
        print(array)
