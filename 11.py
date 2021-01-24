input_list = []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x>=y:
        input_list.append(str(y)+" "+str(x))
    else:
        input_list.append(str(x)+" "+str(y))
for i in input_list:
    print('{0}'.format(i))
