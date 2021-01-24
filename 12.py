def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

# print(make_divisors(80))
a, b,c = map(int, input().split())
divisor_list = make_divisors(c)
sum = 0
for i in range(a,b+1):
    if i in divisor_list:
        sum+=1
print(sum)
