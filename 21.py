N = int(input())
num_list = list(map(int, input().split()))
# num_list.sort(reverse=True)
for n in range(N):
    if n == N-1:
        print(num_list[N-n-1])
    else:
        print(num_list[N-n-1],'',end='')
