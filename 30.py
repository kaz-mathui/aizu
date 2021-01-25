result_list = []
while True:
    s = input()
    if s == '0':
        break
    sum = 0
    for sub in range(len(s)):
        sum += int(s[sub])
    result_list.append(sum)
for i in result_list:
    print(i)