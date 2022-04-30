# https://programmers.co.kr/learn/courses/30/lessons/17676
def solution(lines):
    times, answer = [], 0

    # 파싱, times 에 [시작, 끝] 차례대로 입력
    for log in lines:
        info = log.split()
        time = info[1].split(':')
        # 시간 모두 초 단위로 변경
        end = int(time[0]) * 3600 + int(time[1]) * 60 + float(time[2])
        # 시작과 끝을 포함하므로 최소단위 0.001 더함
        start = end - float(info[2].rstrip('s')) + 0.001

        times.append([start, end])

    # 끝나는 시각 기준 + 1초 까지의 처리량만 보면 됨
    for i in range(len(times)):
        s, e = times[i]
        count = 1
        # 끝나는 시각이 오름차순으로 정렬되어 있으므로 뒷 부분만 탐색해도 됨
        for j in range(i + 1, len(times)):
            # 탐색중인 로그의 시작 시각이 1초 구간 내 혹은 앞에 있으면 처리량 증가
            # 시간은 시작 포함이므로 < 이어야 함
            if times[j][0] < e + 1:
                count += 1

        answer = max(answer, count)

    return answer
