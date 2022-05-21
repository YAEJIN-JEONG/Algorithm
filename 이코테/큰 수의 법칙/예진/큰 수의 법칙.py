# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더해 가장 큰수를 만드는 법칙
# 단, 배열의 특정 인덱스에 해당하는 수가 연속헤서 K번을 초과하여 더해질 수 는 없다
# 서로 다른 인덱스에 해당하는 수가 같은 경우에도 다른 것으로 간주

# -> 가장 큰 수를 k번 더하고 두번째로 큰수 한번 더하고 다시 가장 큰 수 더하기 반복
n,m,k = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
first = array[n-1]
second = array[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -=1
    if m ==0 :
        break
    result += second
    m -=1

print(result)

