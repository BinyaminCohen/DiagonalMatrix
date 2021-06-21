def counter(num, list):
    return sum([1 if num == i else 0 for i in list])


print(counter(5, [5, 4, 5, 5, 2]))

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def diagonal(matrix):
    length = len(matrix)
    return [[matrix[i][j] * 2 if i == j else matrix[i][j] * 0 for j in range(length)] for i in range(length)]


d = diagonal(matrix)
print(d)
