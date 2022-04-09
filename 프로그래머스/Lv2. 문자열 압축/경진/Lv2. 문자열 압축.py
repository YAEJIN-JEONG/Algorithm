# https://programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    answer = len(s)

    # 문자열 자르는 단위: 1 ~ 문자열 길이의 절반
    for i in range(1, len(s) // 2 + 1):
        # 문제 조건에서 앞에서부터 차례대로 자른다고 했으므로 자르고 시작
        sliced = s[:i]
        length = 0  # 압축 문자열 길이
        cnt = 1     # 단위 문자열 세기

        # i개 단위로 자르므로 i씩 증가, 나머지가 남을 수 있으므로 길이에 i 더해줌
        for j in range(i, len(s) + i, i):
            # 이전 단위문자열과 일치하는지에 따라 분기
            if sliced == s[j:j+i]:
                cnt += 1
            else:
                length += len(sliced)
                # 단위 문자열 갱신
                sliced = s[j:j+i]
                # cnt > 1 이면 압축된 것. 결과만큼 길이 더하기
                if cnt > 1:
                    length += len(str(cnt))
                cnt = 1

        answer = min(answer, length)

    return answer
