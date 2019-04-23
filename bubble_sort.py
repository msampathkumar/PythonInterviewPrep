'''
The Bubble Sort
The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.


http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
'''

def iterator(data, last_index):
    for i in range(0, last_index):
        j = i + 1
        print(data[i] , data[j])
        if not (data[i] <= data[j]):
            temp = data[i]
            data[i] = data[j]
            data[j] = temp


def merge_data(data):
    _merging_data = True
    while _merging_data:
        _new_data = []
        for i, new in enumerate(data[1:]):
            prev = data[i-1]
            if prev[1] > new[0]:
                _new_data.append()


def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        # iterator(data, )
        iterator(data, i)
        print(data)


if __name__ == '__main__':
    # ground truth
    print('---' * 15)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(sample_data)
    iterator(sample_data, len(sample_data) - 1)
    print(sample_data)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubble_sort(sample_data)
    print(sample_data == sorted(sample_data))
