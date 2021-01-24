N = int(input())
for i in range(3,N+1):
    # print(i)
    if i % 3 == 0:
        # t = i
        print('',str(i),end='')
        if i == N:
            print("")
        continue
    x = i
    while x >= 1:
        if x % 10 == 3:
            print('',str(i),end='')
            if i == N:
                print("")
            break
        x = int(x / 10)
    if i == N:
        print("")
