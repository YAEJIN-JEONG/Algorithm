# https://programmers.co.kr/learn/courses/30/lessons/42627
import heapq


def solution(jobs):
    time, answer, n = 0, 0, len(jobs)
    # 요청시각이 빠른 순서대로, 요청시각이 같다면 소요시간이 짧은 순서대로 정렬
    jobs.sort(key=lambda j: j[1])
    jobs.sort(key=lambda j: j[0])

    while jobs:
        # 현재 시각에서 요청 중인 작업이 있으면 소요시간이 짧은 작업을 우선으로 처리
        # 현재 요청 중인 작업이 없으면, 다음 요청시각으로 이동
        time = max(time, jobs[0][0])
        # 현재 요청 중인 맨 앞 작업 우선순위 큐에 넣음. cost = 소요시간
        q = []
        job = jobs.pop(0)
        heapq.heappush(q, (job[1], job))

        while q:
            # 우선순위 큐에서 꺼내어 처리
            t, job = heapq.heappop(q)
            answer += time - job[0] + job[1]
            time += job[1]
            # 큐에서 꺼낸 작업을 처리하는 동안 시간은 계속 흐름
            # 변경된 시각에서 요청 중인 작업을 큐에 계속 추가. cost = 소요시간
            while jobs and time >= jobs[0][0]:
                job = jobs.pop(0)
                heapq.heappush(q, (job[1], job))

    return answer // n
