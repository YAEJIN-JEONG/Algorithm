# https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    # 파싱
    s_list = s.lstrip('{').rstrip('}').split('},{')
    # 파싱된 결과를 다시 set() 리스트로 변환
    set_list = [{int(elem) for elem in n_list.split(',')} for n_list in s_list]
    # 길이 기준 정렬
    set_list.sort(key=len)

    # 길이가 1인 원소가 제일 첫 순서
    answer = [list(set_list[0])[0]]
    for i in range(1, len(set_list)):
        # (길이가 n 인 집합)과 (길이가 n - 1 인 집합)의 차집합에 남은 원소가 다음 순서
        answer.append(list(set_list[i] - set_list[i - 1])[0])

    return answer
