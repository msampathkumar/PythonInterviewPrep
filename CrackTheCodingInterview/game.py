
matrix = [
    list(range(10, 15)),
    list(range(15, 20)),
    list(range(20, 25)),
    list(range(25, 30)),
    list(range(30, 35)),
]
#
# matrix = [[1, 2], [3, 4]] # [[3, 1], [4, 2]]
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ] # [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

def print_matrix():
    print('-' * 5)
    for each in matrix:
        print(each)


print_matrix()
# find the center and find the rings
m, n = len(matrix), len(matrix[0])
mid = int(m / 2)
for level in range(0, mid):
    first = level
    last = n - 1 - level
    for offset in range(first, last):
        points = (matrix[first][first + offset], matrix[first + offset][last], matrix[last][last - offset], matrix[last - offset][first])
        # print(points , points[1:] + points[:1])
        (matrix[first][first + offset], matrix[first + offset][last], matrix[last][last - offset],
         matrix[last - offset][first]) = (points[-1], points[0], points[1], points[2])


print_matrix()
print(matrix)
