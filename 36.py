str = input()
N = int(input())
meirei_list = []
for i in range(N):
    meirei = list(input().split())
    meirei_list.append(meirei)
for i in range(N):
    meirei = meirei_list[i]
    if meirei[0] == 'replace':
        str = str[:int(meirei[1])] + meirei[3] + str[int(meirei[2])+1:]
        # print(str)
    elif meirei[0] == 'reverse':
        new_str_list = list(reversed(str[int(meirei[1]):int(meirei[2])+1]))
        
        new_str = ''.join(new_str_list)
        str = str[:int(meirei[1])] + new_str + str[int(meirei[2])+1:]
        # print(str)
    else:
        print(str[int(meirei[1]):int(meirei[2])+1])

    
    # print(meirei)
    # try:
    #     meirei ,hiki1,hiki2,moku = input().split()
    #     # print(meirei ,hiki1,hiki2,moku)
    # except:
    #     meirei ,hiki1,hiki2 = input().split()