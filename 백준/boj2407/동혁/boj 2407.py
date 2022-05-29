import math
n,m = map(int, input().split())

#n!/ n-m! * m!
a = math.factorial(n)
b = math.factorial(n-m) * math.factorial(m)

print(a//b)