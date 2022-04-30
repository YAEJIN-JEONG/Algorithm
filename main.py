import sys
n = int(sys.stdin.readline().strip())

li = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    li.append((a,b))
li.sort(key=lambda x: (x[1],x[0]))

s=count=0
for i in li:
    if s<= i[0]:
        s=i[1]
        count+=1
print(count)

