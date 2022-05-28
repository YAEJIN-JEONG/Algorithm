# https://programmers.co.kr/learn/courses/30/lessons/86971
def solution(n, wires):
    answer = n
    for i in range(len(wires)):
        # i 번째 전선을 끊는 경우
        sub_wires = wires[:i] + wires[i+1:]
        nodes = set(sub_wires[0])

        # sub_wires 길이 만큼 반복 업데이트
        for _ in range(len(sub_wires)):
            for sub in map(set, sub_wires):
                # 교집합 해서 공집합이 아니면 union
                if nodes & sub:
                    nodes |= sub

        # 한쪽 송전탑 개수가 k 면 다른 쪽은 n - k
        # abs(k - (n - k)) = abs(2 * k - n)
        answer = min(answer, abs(2 * len(nodes) - n))

    return answer
