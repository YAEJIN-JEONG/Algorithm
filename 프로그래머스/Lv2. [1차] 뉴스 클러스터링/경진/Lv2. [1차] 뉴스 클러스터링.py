# https://programmers.co.kr/learn/courses/30/lessons/17677
def elem_counter(s):
    # {원소: 개수} counter 만들기
    counter = {}
    for i in range(len(s) - 1):
        now = s[i] + s[i + 1]

        if now.isalpha():
            counter[now] = counter.get(now, 0) + 1

    return counter


def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    counter1, counter2 = elem_counter(str1), elem_counter(str2)

    union, inter = {}, {}
    for k in set(counter1.keys()) | set(counter2.keys()):
        # union 은 개수 더 많은 것 선택, default = 0
        union[k] = max(counter1.get(k, 0), counter2.get(k, 0))
        # intersection 은 개수 더 적은 것 선택, default = 0
        inter[k] = min(counter1.get(k, 0), counter2.get(k, 0))

    union_cnt = sum(union.values())
    inter_cnt = sum(inter.values())

    if union_cnt == 0:
        return 65536

    return int(inter_cnt / union_cnt * 65536)
