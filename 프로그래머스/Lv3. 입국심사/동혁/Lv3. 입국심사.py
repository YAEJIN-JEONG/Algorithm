def solution(n, times):
    #최저는 1분씩 심사하는 경우
    #최대는 가장 느린 심사관한테 모두 받는 경우
    low, high = 1,max(times)*n

    while low <= high:

        #중간값
        mid = (low + high)//2
        #검사한 사람의 수
        people = 0

        #mid분동안 심사한 사람의 수
        for i in times:
            people += mid // i
            #mid분동안 n명 이상의 심사를 한 경우 탈출
            if people >= n:
                break

        #심사한 사람의 수가 n보다 많거나 같은 경우
        if people>=n:
            high = mid-1
        #심사한 삼사의 수가 n보다 적은 경우
        elif people < n:
            low = mid+1

    return low
