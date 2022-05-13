# https://programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    # 알파벳 별 조이스틱 상하 최소 횟수
    change_cost = [min(ord(alpha) - ord('A'), ord('Z') - ord(alpha) + 1) for alpha in name]
    answer = sum(change_cost)
    # 조이스틱 좌우 최소 횟수
    min_dist = len(name) - 1

    for i in range(len(name) - 1):
        cnt = 1
        for c in name[i + 1:]:
            if c == 'A':
                cnt += 1
            else:
                break

        # 이동해야 하는 다음 인덱스 (연속된 'A' 만큼 건너 뛴 인덱스)
        next_index = i + cnt
        # 1. min_dist
        # 2. 현재 인덱스 i 까지 오른쪽 이동, 다시 next_index 까지 왼쪽 이동
        # 3. next_index 까지 왼쪽 이동, 다시 i 까지 오른쪽 이동
        # 1, 2, 3 중에 최소값으로 갱신
        min_dist = min(min_dist, 2 * i + (len(name) - next_index), 2 * (len(name) - next_index) + i)

    # 구한 좌우 최소 횟수 더하기
    answer += min_dist
    return answer
