from decimal import Decimal
import math
# getcontext().prec = 8
a,b,C = map(Decimal, input().split())
sinC = Decimal(math.sin(math.radians(C)))
S = Decimal(0.5) * a * b * sinC
c = Decimal(math.sqrt(a**Decimal(2)+b**Decimal(2)-Decimal(2)*a*b*Decimal(math.cos(math.radians(C)))))
L = a+b+c
h = Decimal(2) * S * Decimal(1) / a
print('{0:.8f}'.format(S))
print('{0:.8f}'.format(L))
print('{0:.8f}'.format(h))
# print(drink)