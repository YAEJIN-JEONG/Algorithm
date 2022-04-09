# https://programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    # 닉네임 uid: nickname 형태로 딕셔너리에 저장
    nickname, answer = {}, []
    str_template = ["님이 들어왔습니다.", "님이 나갔습니다."]

    for r in record:
        info = r.split()
        # 행위에 따라 분기, 출력문에서 닉네임이 들어갈 공간에는 uid 적기
        if len(info) < 3:
            answer.append(info[1] + str_template[1])
        elif info[0] == 'Enter':
            nickname[info[1]] = info[2]
            answer.append(info[1] + str_template[0])
        else:
            nickname[info[1]] = info[2]

    # uid 로 적어두었던 곳 nickname 으로 변경
    for i in range(len(answer)):
        # uid 추출
        uid = answer[i].rstrip(str_template[0]).rstrip(str_template[1])
        # 최종 출력문으로 변경 uid -> nickname
        answer[i] = answer[i].replace(uid, nickname[uid])

    return answer
