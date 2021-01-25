n,m,l = map(int, input().split())
mat1 = [[0] * (m) for i in range(n)]
mat2 = [[0] * (l) for i in range(m)]
for i in range(n):
    mat1[i] = list(map(int, input().split()))
for j in range(m):
    mat2[j] = list(map(int, input().split()))
result_mat = [[0] * (l) for i in range(n)]
for i in range(n):
    for j in range(l):
        result_mat[i][j] = sum([mat1[i][k]*mat2[k][j] for k in range(m)])
for i in range(n):
    matrix_str=[str(a) for a in result_mat[i]]
    print(' '.join(matrix_str))