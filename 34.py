# test = 'abcdef'
# test = test[2:] + test[:2]
# print(test)
result_list = []
while True:
    input_data = input()
    if input_data == '-':
        break
    num = int(input())
    for i in range(num):
        shuffle = int(input())
        input_data = input_data[shuffle:] + input_data[:shuffle]
    result_list.append(input_data)
for i in result_list:
    print(i)