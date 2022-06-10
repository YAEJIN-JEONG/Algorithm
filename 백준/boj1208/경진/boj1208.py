# https://www.acmicpc.net/problem/1208
# 부분수열의 합 2
from sys import stdin
from itertools import combinations
from bisect import bisect_left, bisect_right

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

# 반으로 나누기
left, right = arr[:len(arr) // 2], arr[len(arr) // 2:]

# 각각 모든 조합들의 합 구하기
sum_left, sum_right = [], []
for i in range(1, len(left) + 1):
    sum_left.extend(list(map(sum, combinations(left, i))))

for i in range(1, len(right) + 1):
    sum_right.extend(list(map(sum, combinations(right, i))))

# 이분탐색을 위해 정렬
sum_left.sort()
sum_right.sort()

# 왼쪽이나 오른쪽에서만 합이 s가 되는 경우 찾기
answer = bisect_right(sum_left, s) - bisect_left(sum_left, s)
answer += bisect_right(sum_right, s) - bisect_left(sum_right, s)

# 왼쪽 + 오른쪽에서 합이 s가 되는 경우 찾기
for elem in sum_left:
    target = s - elem
    answer += bisect_right(sum_right, target) - bisect_left(sum_right, target)

print(answer)
