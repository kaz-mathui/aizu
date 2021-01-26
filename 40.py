from decimal import Decimal
N = int(input())
x_vec = list(map(int,input().split()))
y_vec = list(map(int,input().split()))
dis_1 = 0
dis_2 = 0
dis_3 = 0
dis_inf_list = []
for i in range(N):
    dis_1 += abs(x_vec[i]-y_vec[i])
    dis_2 += (x_vec[i]-y_vec[i])**2
    dis_3 += abs((x_vec[i]-y_vec[i])**3)
    dis_inf_list.append(abs(x_vec[i]-y_vec[i]))
print(dis_1)
dis_2_ans = dis_2 ** Decimal(1/2)
dis_3_ans = dis_3 ** Decimal(1/3)
print(dis_2_ans)
print(dis_3_ans)
print(max(dis_inf_list))