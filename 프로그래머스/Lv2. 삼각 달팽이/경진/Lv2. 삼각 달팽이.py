# https://programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    triangle = [[0] * i for i in range(1, n + 1)]
    triangle[0][0] = 1
    x, y = 0, 0

    # 순서: 내려가기 -> 오른쪽 -> 올라가기
    steps = [[1, 0], [0, 1], [-1, -1]]
    idx, end = 2, n * (n + 1) // 2

    # idx 가 end 를 넘으면 종료
    while idx <= end:
        # (내려가기 -> 오른쪽 -> 올라가기) 순서대로
        # 단계별로 범위를 벗어나지 않고, 처리하지 않은 곳 까지 진행
        for step in steps:
            while True:
                nx, ny = x + step[0], y + step[1]

                if 0 <= nx < len(triangle) and 0 <= ny < len(triangle[nx]) and triangle[nx][ny] == 0:
                    x, y = nx, ny
                    triangle[x][y] = idx
                    idx += 1
                else:
                    break

    answer = []
    for row in triangle:
        answer.extend(row)

    return answer
