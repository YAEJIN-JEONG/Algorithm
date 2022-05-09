def solution(numbers):
    li = [i for i in range(10)]

    #있는 숫자 제거(중복이 없어서 가능)
    for i in numbers:
        li.remove(i)
    return sum(li)