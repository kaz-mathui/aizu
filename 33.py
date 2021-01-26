# import re
W = input()
input_list = []
while True:
    texts = list(input().split())
    if texts[0] == 'END_OF_TEXT':
        break
    input_list.append(texts)
count = 0
for i in range(len(input_list)):
    for j in range(len(input_list[i])):
        # if re.compile(input_list[i][j],re.IGNORECASE).match(W) != None:
        if input_list[i][j].upper() == W.upper():
            count += 1
            # print(input_list[i][j])
print(count)
