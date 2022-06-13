# https://www.acmicpc.net/problem/1806
# 부분합
from sys import stdin

n, s = map(int, stdin.readline().split())
n_list = list(map(int, stdin.readline().split()))
n_list.insert(0, 0)

# 정답, right pointer, 누적 합
answer, rp, total = len(n_list), 0, 0

# i 는 left pointer
for i in range(len(n_list)):
    # left pointer 를 오른쪽으로 이동 (누적 합 에서 빼주기)
    total -= n_list[i]

    # 누적 합이 s 보다 크거나 같아질 때 까지 rp 를 오른쪽으로 이동
    while total < s and rp < len(n_list) - 1:
        rp += 1
        total += n_list[rp]

    # 누적 합이 s 이상 이면 정답 갱신
    if total >= s:
        answer = min(answer, rp - i)

print(answer if answer < len(n_list) else 0)
