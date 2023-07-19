def binary_search(my_list: list, value) -> list:
    def _binary_search_rec(my_list: list, value, left: int, right: int):
        if left > right:
            return -1
        mid = (left + right) // 2
        if my_list[mid] == value:
            return mid
        elif my_list[mid] > value:
            return _binary_search_rec(my_list, value, left, mid - 1)
        else:
            return _binary_search_rec(my_list, value, mid + 1, right)

    return _binary_search_rec(my_list, value, 0, len(my_list) - 1)


list1 = [1, 4, 7, 9, 12, 15, 17, 19]
list2 = [45, 49, 59, 61, 67, 79, 88, 99]


