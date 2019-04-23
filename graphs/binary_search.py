def recursive_binary_search(alist, start, end, find_val):
    mid_val = int(len(alist[start:end]) / 2) + start
    print((start, mid_val, end, find_val))
    if alist[start] == find_val or alist[end] == find_val:
        return True
    if (start < end) and (find_val > alist[start]) and (find_val < alist[end]):
        return recursive_binary_search(alist, start, mid_val, find_val) or\
               recursive_binary_search(alist, mid_val + 1, end, find_val)
    return False


def linear_binary_search(alist, find_value):
    left_pointer = 0
    right_pointer = len(alist) - 1
    while left_pointer < right_pointer:
        if alist[left_pointer] == find_value:
            return True


if __name__ == '__main__':
    sample_data = list(range(0, 121))
    print(recursive_binary_search(sample_data, 0, len(sample_data) - 1, 15))
    print(linear_binary_search(sample_data, 15))
