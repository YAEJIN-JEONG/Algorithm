import sys
total = int(sys.stdin.readline().strip())
t = int(sys.stdin.readline().strip())
result=0

for i in range(t):
    price, count = map(int, sys.stdin.readline().strip().split())
    result += price*count

if total == result:
    print("Yes")
else:
    print("No")