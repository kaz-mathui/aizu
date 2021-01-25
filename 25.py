result_list = []
while True:
    m,f,r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    elif m == -1 or f == -1:
        result_list.append('F')
    elif m+f >= 80:
        result_list.append('A')
    elif 65 <= m+f < 80:
        result_list.append('B')
    elif 50 <= m+f < 65:
        result_list.append('C')
    elif 30 <= m+f < 50:
        if r >= 50:
            result_list.append('C')
        else:
            result_list.append('D')
    else:
        result_list.append('F')
for i in result_list:
    print(i)