# https://programmers.co.kr/learn/courses/30/lessons/42895
def solution(n, number):
    answer = -1
    # N 최대사용 횟수는 8 이므로 N을 1~8번 사용했을때 까지만 구함
    # 초기값 1: {N}, 2: {NN}, 3: {NNN} ...
    result_set = {i: {int(str(n) * i)} for i in range(1, 9)}

    # N을 i번 사용해서 만들 수 있는 수 구하기
    for i in range(2, 9):
        # N을 j번 사용해서 만드는 수와
        # N을 i-j 번 사용해서 만드는 수의 사칙연산 결과를 추가
        for j in range(1, i):
            for a in result_set[j]:
                for b in result_set[i - j]:
                    result_set[i].add(a + b)
                    result_set[i].add(abs(a - b))
                    result_set[i].add(a * b)
                    if b > 0:
                        result_set[i].add(a // b)
                    if a > 0:
                        result_set[i].add(b // a)

    # 정답 구하기
    for k, v in result_set.items():
        if number in v:
            answer = k
            break

    return answer
