def bubble_sort(list_):
    is_list_sorted = False
    for i in range(len(list_) - 1):
        if is_list_sorted:
            break
        for y in range(len(list_) - 1):
            is_list_sorted = True
            if list_[y] > list_[y + 1]:
                is_list_sorted = False
                tmp = list_[y]
                list_[y] = list_[y + 1]
                list_[y + 1] = tmp


if __name__ == "__main__":
    list_to_sort = [31, 1, 35, 52, 8, 9, 6, 34, 55, 22, 12, 53, 87, 54]
    bubble_sort(list_to_sort)
    print(list_to_sort)
