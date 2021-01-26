import statistics
import math
data_set= []
while True:
    num = int(input())
    if num == 0:
        break
    data_list = list(map(int,input().split()))
    data_set.append(data_list)
for i in range(len(data_set)):
    data_list = data_set[i]
    standard = statistics.pstdev(data_list)
    print(standard)
