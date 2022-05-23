def solution(s):
    answer = []

    #중괄호 분리
    s_list=s[2:-2].split('},{')

    #각 원소의 길이를 기준으로 정렬
    s_list.sort(key=len)

    for i in s_list:
        #원소내 ,분리 및 정수로 형변환
        numbers =list(map(int,i.split(',')))

        # numbers의 숫자를 하나씩 접근하며 답 리스트에 없는 경우에만 append
        for number in numbers:
            if number not in answer:
                answer.append(number)
    return answer