# https://programmers.co.kr/learn/courses/30/lessons/68936
answer = [0, 0]


# 시작 좌표, 크기
def rec(arr, x, y, size):
    global answer

    if is_match(arr, x, y, size):
        answer[arr[x][y]] += 1
    else:
        size //= 2
        # 4영역 분할 후 재귀
        for i in range(2):
            for j in range(2):
                rec(arr, x + (size * i), y + (size * j), size)


# 영역 내 모든 원소 일치 여부
def is_match(arr, x, y, size):
    k = arr[x][y]
    for i in range(x, x + size):
        for j in range(y, y + size):
            if arr[i][j] != k:
                return False
    return True


def solution(arr):
    global answer
    # 재귀
    rec(arr, 0, 0, len(arr))
    return answer
