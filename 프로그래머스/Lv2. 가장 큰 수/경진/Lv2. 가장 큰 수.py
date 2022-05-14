# https://programmers.co.kr/learn/courses/30/lessons/42746
def solution(numbers):
    n_list = []
    # 숫자들은 최대 1000 이므로 네 자리 숫자 맞추기
    for n in map(str, numbers):
        n_list.append([(n * 4)[:4], len(n)])

    # 내림차순 정렬
    n_list.sort(key=lambda x: x[0], reverse=True)

    answer = []
    # 원래 길이로 반환하며 숫자 만들기
    for n, length in n_list:
        answer.append(n[:length])

    return str(int(''.join(answer)))
