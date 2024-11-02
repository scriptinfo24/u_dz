def get_matrix(n, m, value):
    for i in range(n-1):
        matrix = []
        matrix.append([value] * m)
        for j in range(n-1):
            matrix.append([value] * m)
    return matrix

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

print(result1)
print(result2)
print(result3)
