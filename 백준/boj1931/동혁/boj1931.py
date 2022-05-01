import sys
n = int(sys.stdin.readline().strip())
li = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    li.append((a,b))
#회의가 끝나는 순서, 회의가 시작하는 순서로 정렬
li.sort(key=lambda x: (x[1],x[0]))

#시작시간이 직전 회의보다 시간이 적거나 같으면 count++
s=0
count=0
for i in li:
    if s<= i[0]:
        s=i[1]
        count+=1
print(count)
