# https://programmers.co.kr/learn/courses/30/lessons/42576
from collections import Counter


def solution(participant, completion):
    # 이름이 같을 수 있기 때문에 {이름: 횟수, ...} 로 사전 만듬
    participant_counter = Counter(participant)

    for s in completion:
        # completion 에 있는 이름의 횟수 -1, 횟수가 0이면 제거
        participant_counter[s] -= 1
        if participant_counter[s] == 0:
            participant_counter.pop(s)

    # 마지막 남은 key(이름) 반환
    return list(participant_counter.keys())[0]
