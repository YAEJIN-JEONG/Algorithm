import itertools


# 소수가 맞는지
def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


def solution(numbers):
    numbers, visited, answer = list(numbers), set(), 0

    for i in range(1, len(numbers) + 1):
        # i 개 뽑는 순열
        for p in itertools.permutations(numbers, i):
            now = int(''.join(p))

            if now not in visited:
                visited.add(now)

                if is_prime(now):
                    answer += 1

    return answer
