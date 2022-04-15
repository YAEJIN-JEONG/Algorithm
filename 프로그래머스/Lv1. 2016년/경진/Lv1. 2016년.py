# https://programmers.co.kr/learn/courses/30/lessons/12901
def solution(a, b):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    # 1월 1일부터 며칠지났는지?
    # (1 ~ a-1 월 까지 날짜 합) + b일 + (원래 금요일이니까 + 4)
    # 지난 날짜를 7로 나눈 나머지가 요일 인덱스
    return day[(sum(days[:a]) + b + 4) % len(day)]
