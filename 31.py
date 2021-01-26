
alphabet = 'abcdefghijklmnopqrstuvwxyz'
input_str = ''
while True:
    try:
        input_str += input().lower()
    except EOFError:
        break

# input_str = []
# for l in sys.stdin:
#     input_str.append(l.lower())

for i in range(26):
    s = alphabet[i]
    # print(s)
    count = 0
    for j in range(len(input_str)):
        if input_str[j] == s:
            count += 1
    print(s,':',count)