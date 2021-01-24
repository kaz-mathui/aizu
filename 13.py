a, b = map(int, input().split())
# print(int(a/b),int(a%b),float(a/b))
# print("{0} {1} {2:.5f} {2:.6f}".format(a, b, c))   # 1.0 3.1415 1.41421 1.414214
print("{0:d} {1:d} {2:.5f}".format(int(a/b), int(a%b), a/b))   # 1.0 3.1415 1.41421 1.414214