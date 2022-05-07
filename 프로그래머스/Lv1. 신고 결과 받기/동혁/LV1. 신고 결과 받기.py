def solution(id_list, report, k):
    from collections import defaultdict

    li = defaultdict(list)
    stop = []   #정지 명단
    result = [0 for i in range(len(id_list))]

    # 정지대상자: [신청자1, 신청자 2...]로 만들기
    for i in report:
        a, b = i.split()

        #중복신청시 거부
        if a in li[b]:
            continue
        li[b].append(a)

    #목표 숫자만큼 신고를 당한사람을 구함
    for i in li:
        if len(li[i]) >= k:
            stop.append(i)

    #정지단한 사람의 키에 해당하는 밸류의 사람에게 메세지 추가
    for i in li:
        if i in stop:
            for j in li[i]:
                result[id_list.index(j)] += 1

    return result