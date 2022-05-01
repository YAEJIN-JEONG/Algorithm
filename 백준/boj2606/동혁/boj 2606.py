import sys
n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

#이중 배열 생성
li = [[] for i in range(n+1)]

#a,b를 입력 받아서 두 원소가 서로를 가리키게 할당
for i in range(m):
    a,b = map(int, sys.stdin.readline().strip().strip().split())
    li[a].append(b)
    li[b].append(a)

#시작 노드로 1 지정
result = [1]

#감염된 노드가 가리키고 있는 원소들중 감염되지 않은 노드를 감염
for i in result:
    for j in li[i]:
        if j not in result:
            result.append(j)

#1에서 부터 감염된 수를 찾는 문제이기 때문에 -1
print(len(result)-1)