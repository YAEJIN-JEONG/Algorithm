import sys

n,k =map(int,sys.stdin.readline().strip().split())
li=[]

#액면권이 큰 순서부터 거슬러 주면 거스름 동전의 수가 최소가 된다
for i in range(n):
    li.append(int(sys.stdin.readline().strip()))
li.reverse()

count = 0
for i in li:
    count += k//i
    k = k % i

print(count)
