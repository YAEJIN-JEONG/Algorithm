def rec(a, b):
    if a == b:
        return 1

    return 1 + rec(a // 2, b // 2)


def solution(n, a, b):
    # 처음에 몇 번째 조 였는지 넘겨서 반씩 줄이기
    return rec((a - 1) // 2, (b - 1) // 2)
