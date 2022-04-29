import sys
input = sys.stdin.readline().strip()

#문자열을 분리 '-'
li = input.split('-')
s=0

#첫번쨰 마이너스를 만나기 전까지는 플러스
for i in li[0].split('+'):
    s+= int(i)

#값을 최소로 만들어야 되기 때문에 -(a+b+c)같은 형태로 만들어서 계산
for i in li[1:]:
    for j in i.split('+'):
        s-= int(j)

print(s)