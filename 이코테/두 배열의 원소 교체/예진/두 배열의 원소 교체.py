#두 배열은 N개 원소, K번 바꿔치기 연산하여 배열 A의 원소의 합이 최대가 되도록
n,k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True) #내림차순 정렬

for i in range(k):
    if a[i] < b[i]:
        a[i],b[i]= b[i],a[i]
    else:
        break

print(sum(a))