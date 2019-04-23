'''
The Selection Sort
The selection sort improves on the bubble sort by making only one exchange for every pass through the list. In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location.


http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
'''


def iterator(data, last_index):
    i = 0
    max_index, max_value = i, data[i]
    for i in range(1, last_index):
        if data[i] > data[max_index]:
            max_index, max_value = i, data[i]
    # print(max_index, max_value, last_index, data[last_index])
    if data[max_index] > data[last_index]:
        tmp = data[max_index]
        data[max_index] = data[last_index]
        data[last_index] = tmp


def selection_sort(data):
    for i in range(len(data) - 1, 0, -1):
        # iterator(data, )
        iterator(data, i)


if __name__ == '__main__':
    # ground truth
    print('---' * 15)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(sample_data)
    iterator(sample_data, len(sample_data) - 1)
    print(sample_data)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(sample_data)
    print(sample_data == sorted(sample_data))
