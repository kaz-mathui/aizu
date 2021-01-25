N = int(input())
S_list = []
H_list = []
C_list = []
D_list = []
for i in range(N):
    mark, num = input().split()
    num = int(num)
    if mark == 'S':
        S_list.append(num)
    elif mark == 'H':
        H_list.append(num)
    elif mark == 'C':
        C_list.append(num)
    else:
        D_list.append(num)
for i in range(1,14):
    # print(i)
    if not i in S_list:
        print('S',i)
for i in range(1,14):
    # print(i)
    if not i in H_list:
        print('H',i)
for i in range(1,14):
    # print(i)
    if not i in C_list:
        print('C',i)
for i in range(1,14):
    # print(i)
    if not i in D_list:
        print('D',i)