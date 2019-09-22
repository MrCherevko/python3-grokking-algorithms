def binary_search(searching_list, item):
    low = 0
    high = len(searching_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = searching_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    number_list = [1, 3, 5, 7, 9]
    print(binary_search(number_list, 9))
