def insertion_sort(data):
    for i in range(1, len(data)):
        pos = i
        remember = data[pos]
        while pos > 0 and data[pos - 1] > remember:
            data[pos] = data[pos - 1]
            pos = pos - 1
        data[pos] = remember
        print(data)


if __name__ == '__main__':
    # ground truth
    print('---' * 15)
    # sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(sample_data)
    # iterator(sample_data, 2)
    # print(sample_data)
    # sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    # print(insertion_sort(sample_data))
    # print(sample_data == sorted(sample_data))
    # iterator([1, 3, 5, 7, 4.5, 10, 11, 12], 4)
    insertion_sort(list(reversed([1, 3, 5, 7, 4.5, 10, 11, 12])))
