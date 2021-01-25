# input_str = input()
# judge_str = input()
# if judge_str in input_str+input_str:
#     print("Yes")
# else:
#     print("No")

# coding: utf-8

s = input()
p = input()
flg = False

for i in range(len(s)):
    if p in s:
        flg = True
        break
    s = s[1:] + s[:1]

if flg:
    print('Yes')
else:
    print('No')