# https://www.acmicpc.net/problem/16566
# 카드 게임
from sys import stdin


# 이분 탐색 - upper bound
def upper_bound(num):
    global cards

    low, high = 0, len(cards) - 1

    while low < high:
        mid = (low + high) // 2

        if cards[mid] > num:
            high = mid
        else:
            low = mid + 1

    return high


# 부모 인덱스 찾기
def get_parent(index):
    global nxt

    if nxt[index] == index:
        return index

    new_index = get_parent(nxt[index])
    # 다음번 호출 시 recursion depth 를 줄이기 위해 갱신
    nxt[index] = new_index

    return new_index


if __name__ == '__main__':
    n, m, k = map(int, stdin.readline().split())
    cards = sorted(list(map(int, stdin.readline().split())))
    order = list(map(int, stdin.readline().split()))
    # 부모 인덱스 저장
    nxt = [i for i in range(n)]

    for i in order:
        idx = get_parent(upper_bound(i))
        print(cards[get_parent(idx)])
        # 연결 시키기
        nxt[get_parent(idx)] = get_parent(idx + 1)
