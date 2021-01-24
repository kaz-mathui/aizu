input_list = []
while True:
    x, op , y = input().split()
    if op == "?":
        break
    if op == "+":
        input_list.append(int(x)+int(y))
    elif op == "-":
        input_list.append(int(x)-int(y))
    elif op == "*":
        input_list.append(int(x)*int(y))
    elif op == "/":
        input_list.append(int(int(x)/int(y)))
for i in input_list:
    print('{0}'.format(i))
