# https://www.acmicpc.net/problem/2096
# 내려가기
# 메모리 제한이 있음. 데이터들 저장해두지 않고 그때 그때 처리
from sys import stdin

n = int(stdin.readline())

# 맨 첫 줄만 읽어서 정보 저장
prev_max = list(map(int, stdin.readline().split()))
prev_min = prev_max.copy()

# 최대, 최소 값 dp 배열
dp_max, dp_min = prev_max.copy(), prev_min.copy()

for i in range(1, n):
    # 한 줄씩 읽으면서 dp 배열 갱신
    a, b, c = map(int, stdin.readline().split())

    dp_max[0] = max(prev_max[0], prev_max[1]) + a
    dp_max[1] = max(prev_max) + b
    dp_max[2] = max(prev_max[1], prev_max[2]) + c

    dp_min[0] = min(prev_min[0], prev_min[1]) + a
    dp_min[1] = min(prev_min) + b
    dp_min[2] = min(prev_min[1], prev_min[2]) + c

    prev_max = dp_max.copy()
    prev_min = dp_min.copy()

print(max(dp_max), min(dp_min))
