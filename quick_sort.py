# http://interactivepython.org/runestone/static/pythonds/SortSearch/TheQuickSort.html

# def find_pivot_point(data, left_pointer, right_pointer):
#     pivot_value = data[left_pointer]
#     pointer1 = left_pointer
#     pointer2 = right_pointer
#     not_sorted = True
#     while not_sorted:
#         while pointer1 <= pointer2 and data[pointer1] <= pivot_value:
#             pointer1 = pointer1 + 1
#         while pointer1 <= pointer2 and data[pointer2] >= pivot_value:
#             pointer2 = pointer2 - 1
#         if pointer2 < pointer1:
#             not_sorted = False
#         else:
#             tmp = data[pointer1]
#             data[pointer1] = data[pointer2]
#             data[pointer2] = tmp
#     tmp = data[pointer2]
#     data[pointer2] = pivot_value
#     data[left_pointer] = tmp
#     return pointer2
#
#
def swap(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = data[i]


def find_pivot_point(data, start, end):
    pivot_value = data[start]
    left_pointer = start + 1
    right_pointer = end
    while True:
        while left_pointer <= right_pointer and data[left_pointer] <= pivot_value:
            left_pointer = left_pointer + 1
        while left_pointer <= right_pointer and data[right_pointer] >= pivot_value:
            right_pointer = right_pointer - 1
        if left_pointer > right_pointer:
            break
        else:
            tmp = data[left_pointer]
            data[left_pointer] = data[right_pointer]
            data[right_pointer] = tmp

    tmp = data[start]
    data[start] = data[right_pointer]
    data[right_pointer] = tmp
    return right_pointer


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        while leftmark <= rightmark and pivotvalue <= alist[rightmark]:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)

def quick_sort(data, start, end):
    if start < end:
        pivot_index = find_pivot_point(data, start, end)
        quick_sort(data, start, pivot_index - 1)
        quick_sort(data, pivot_index + 1, end)


if __name__ == '__main__':
    # ground truth
    print('---' * 15)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(sample_data)
    print(partition(sample_data, 0, len(sample_data) - 1))
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quickSortHelper(sample_data, 0, len(sample_data) - 1))
    print(sample_data)
    print('[31, 26, 20, 17, 44, 54, 77, 55, 93]')

    print('---' * 15)
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(sample_data)
    print(find_pivot_point(sample_data, 0, len(sample_data) - 1))
    sample_data = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(quick_sort(sample_data, 0, len(sample_data) - 1))
    print(sample_data)
    print('[31, 26, 20, 17, 44, 54, 77, 55, 93]')



