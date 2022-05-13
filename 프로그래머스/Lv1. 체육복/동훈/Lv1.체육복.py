# https://programmers.co.kr/learn/courses/30/lessons/42862
def solution(n, lost, reserve):
    student=[1 for _ in range(n)]
    #학생 수 만큼 체육복을 가지고 있다고 가정. 1로 초기화
    for i in lost:
            student[i-1] -= 1
    #체육복을 잃어버린 학생 설정
    for i in reserve:
            student[i-1] += 1
    #체육복을 여벌로 가져온 학생 설정
        
    for i in range(n):
        front , rear = i-1 , i+1
        #현재 학생 i의 앞, 뒤의 인덱스 설정
        if student[i] > 1:
        #학생 i 의 체육복의 개수가 2인 경우
            if front >= 0 and student[front] == 0:
                student[front] += 1
                student[i] -= 1
            elif rear <= n-1 and student[rear] == 0:
                student[rear] += 1
                student[i] -= 1
    #학생 i의 앞, 뒤자리 학생의 인덱스를 확인하고, 앞뒤 학생의 체육복을 나눠줌
    answer = n - student.count(0)
    return answer
