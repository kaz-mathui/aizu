n,m = map(int, input().split())
matrix = [[0] * m for i in range(n)]
for i in range(n):
    matrix[i] = list(map(int, input().split()))
vec = [0] * m
for j in range(m):
    # print(j)
    vec[j] = int(input())
# print(matrix,vec)
vec_n = [0] * n
for i in range(n):
    # vec_n[i] = sum([ matrix[i][j] * vec[j] for j in range(m)])
    print(sum([ matrix[i][j] * vec[j] for j in range(m)]))
