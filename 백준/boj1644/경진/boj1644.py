# https://www.acmicpc.net/problem/1644
# 소수의 연속합
from sys import stdin

n = int(stdin.readline())

# n 까지 소수 구하기 (에라토스테네스 채)
is_prime = [True] * (n + 1)
prime_number = [0, 2]

for i in range(2, int(len(is_prime) ** 0.5) + 1):
    if not is_prime[i]:
        continue
    for j in range(2, n // i + 1):
        is_prime[i * j] = False

for i in range(3, len(is_prime)):
    if is_prime[i]:
        prime_number.append(i)

# right pointer, lp + 1 ~ rp 누적 합, 정답 카운트
rp, total, answer = 0, 0, 0
# left pointer 0 부터 시작
for lp in range(len(prime_number)):
    # 이전 숫자 빼주기
    total -= prime_number[lp]

    # 누적 합이 n 보다 작으면 rp 오른쪽으로 이동
    while total < n and rp < len(prime_number):
        total += prime_number[rp]
        rp += 1

    # 누적 합이 n 과 같으면 카운트 증가
    if total == n:
        answer += 1

print(answer)
