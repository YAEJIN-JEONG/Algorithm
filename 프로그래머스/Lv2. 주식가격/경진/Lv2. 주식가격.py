# https://programmers.co.kr/learn/courses/30/lessons/42584
def solution(prices):
    answer = [0] * len(prices)

    stack = []
    for i in range(len(prices)):
        # 스택에서 현재 가격보다 낮은 것 모두 꺼내기
        # 스택에 남은 것들 중, 먼저 들어온 것은 나중에 들어온 것 보다 가격이 낮을 수 밖에 없음
        while stack and stack[-1][1] > prices[i]:
            idx, _ = stack.pop()
            # 떨어지지 않은 시간
            answer[idx] = i - idx

        # (인덱스, 가격) 형태로 스택에 push
        stack.append((i, prices[i]))

    # 끝까지 떨어지지 않은 것들
    for i, p in stack:
        answer[i] = len(prices) - i - 1

    return answer
