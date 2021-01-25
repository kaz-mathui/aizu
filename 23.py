N = int(input())
l_3d = [[[0] * 10 for i in range(3)] for j in range(4)]
# print(l_3d)
for i in range(N):
    b, f, r, v = map(int, input().split())
    l_3d[b-1][f-1][r-1] += v
for x in range(4):
    for y in range(3):
        # [print(z) for z in l_3d[x][y]]
        l_3d_str=[str(a) for a in l_3d[x][y]]
        print('',' '.join(l_3d_str))
    if x == 3:
        break
    print("####################")