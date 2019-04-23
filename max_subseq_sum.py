"""
to find maximum  subsequence sum
"""

def find_max_sub_seq_sum(data, length):
    max_sum_till_now = sum(data[0:length])
    cur_max_sum = max_sum_till_now
    for i in range(1, len(data) - length):
        print(data[i - 1 : i - 1 + length], cur_max_sum)
        cur_max_sum -= data[i - 1]
        cur_max_sum += data[i + 1]


if __name__ == '__main__':
    sample_data = [1, 3, 5, 7, 4.5, 10, 11, 12]
    find_max_sub_seq_sum(sample_data, 3)
