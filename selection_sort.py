

def find_smallest(arr) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(not_sorted_array: list, sort_function: classmethod) -> list:
    sorted_array = []
    for i in range(len(not_sorted_array)):
        smallest = sort_function(not_sorted_array)
        sorted_array.append(not_sorted_array.pop(smallest))
    return sorted_array


if __name__ == '__main__':
    print(selection_sort([5, 3, 6, 2, 10], find_smallest))
