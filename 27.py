r,c = map(int, input().split())
matrix = [[0] * (c+1) for i in range(r+1)]

for i in range(r):
    matrix[i] = list(map(int, input().split()))
    matrix[i].append(0)
# print(matrix)
for i in range(r+1):
    # vec_n[i] = sum([ matrix[i][j] * vec[j] for j in range(m)])
    # print(matrix[i])
    matrix[i][c] = sum(matrix[i])

for j in range(c+1):
    matrix[r][j] = sum([matrix[i][j] for i in range(r)])

for i in range(r+1):
    # print(sum([matrix[i][j] * vec[j] for j in range(m)]))
    matrix_str=[str(a) for a in matrix[i]]
    print(' '.join(matrix_str))