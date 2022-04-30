n,k=map(int,input().split())
result = 0

while True:
    #n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    #n이 k로 나누어 떨어지지 않을 때 가장 가까운 수를 찾을 수 있음
    #n에서 1을 빼는 과정을 몇 번 반복해서 target이라는 값을 만들 수 있고 target은 k로 나누어 떨어지는 수
    target = (n // k) * k

    #총 연산횟수 : 한 번에 1을 빼는 연산을 몇 번 수행할지 넣어줌
    result += (n-target)
    n=target
    # 더 이상 나눌 수 없을 때
    if n<k:
        break
    #k로 나누기
    result+=1
    n//=k

# n이 1보다 크다면 1이 될 수 있도록 남은 수에 1 빼주기
result +=(n-1)
print(result)

#반복문이 수행할 때마다 나누는 연산이 수행되어 로그 시간복잡도