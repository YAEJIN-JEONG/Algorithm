import sys
n = int(sys.stdin.readline().strip())

#(a,b)형태로 리스트에 저장
li = []
for i in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    li.append((a,b))
#끝나는 순서로 정렬 후, 시작하는 순서로 정렬
li.sort(key=lambda x: (x[1],x[0]))

#회의 시작시간이 그 전 타임 회의 끝나는 시간과 같거나 늦으면 선택 후 카운트 추가
s=count=0
for i in li:
    if s<= i[0]:
        s=i[1]
        count+=1
print(count)

