input_list = []
i = 1
while True:
    i = int(input())
    if i == 0:
        break
    input_list.append(i)
    
for x,y in enumerate(input_list):
    print('Case {0}: {1}'.format(x+1, y))
