def solution(nums):
    answer = 0
    # 배열 중 소수가 되는 3개의 숫자 합 -> 조합 itertools.combinations
    from itertools import combinations as cb
    for i in cb(nums, 3):
        temp = sum(i)
        for j in range(2, temp):
            if temp % j == 0:
                break
            else:
                answer += 1
    return answer


