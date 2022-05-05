import sys

n, m = map(int, sys.stdin.readline().strip().split())
#진실을 알고 있는 사람 저장
know = set(sys.stdin.readline().strip().rsplit()[1:])
li = []

#진실을 알고 있는 사람이 없으면 모든 파티 참석 가능
if len(know) == 0:
    print(m)
else:
    #파티에 참가한 사람 저장
    for i in range(m):
        party = set(sys.stdin.readline().strip().split()[1:])
        li.append(party)

    #진실을 알고 있는 사람이 파티원이면(교집합), 파티원 모두가 진실을 알게 된다(합집합)
    #새로이 진실을 알게 된 사람이 다시 진실을 퍼트릴 경우를 위해 파티 수(m) 만큼 반복
    for _ in range(m):
        for i in li:
            if know & i:
                know = know.union(i)

    count = 0
    #최종적으로 진실을 아는 사람이 파티에 없으면  카운트 추가
    for i in li:
        if not know & i:
            count += 1

    print(count)