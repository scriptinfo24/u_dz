def get_matrix(n, m, value):

    for i in range(n):
        matrix = [value]*m
        print(matrix, end=" ")

result1 = get_matrix(2, 2, 10)
print(result1, sep='\n')
result2 = get_matrix(3, 5, 42)
print(result2, sep='\n')
result3 = get_matrix(4, 2, 13)
print(result3, sep='\n')