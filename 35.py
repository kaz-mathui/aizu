N = int(input())
taro_score = 0
hana_score = 0
for i in range(N):
    taro,hana = input().split()
    if taro < hana:
        hana_score += 3
    elif taro > hana:
        taro_score += 3
    else:
        hana_score += 1
        taro_score += 1
print(taro_score,hana_score)