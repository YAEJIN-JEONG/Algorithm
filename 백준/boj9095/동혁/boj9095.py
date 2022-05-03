import sys

#점화식 li[n] = li[n-1] + li[n-2] + li[n-3]
t = int(sys.stdin.readline().strip())
li = []
result = [1,2,4]

#입력받기
for i in range(t):
    li.append(int(sys.stdin.readline().strip()))

#입력값중 최대만큼 경우의 수 계산
for i in range(max(li)):
    result.append(result[i] + result[i+1] + result[i+2])

#해당하는 값의 경우의수 출력
for i in li:
    print(result[i-1])
