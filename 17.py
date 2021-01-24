input_list = []
while True:
    WH = []
    H,W = map(int, input().split())
    if H == 0 and W == 0:
        break
    WH.append(W)
    WH.append(H)
    input_list.append(WH)
for wh in input_list:
    for h in range(wh[1]):
        for w in range(wh[0]):
            print('#',end='')
        print("")
    print("")