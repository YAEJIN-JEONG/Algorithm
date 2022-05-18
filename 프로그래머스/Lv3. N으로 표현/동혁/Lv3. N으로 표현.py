def solution(N, number):
    #DP문제로 5의 갯수를 활용해 dp를 쌓아 나간다
    #5가 2개일 경우 55,10,0,25,1이 나옴
    #5가 3개일 경우 5가 2개인 경우에 나온 숫자로 사칙연산, 555를 만든다

    #N과 Nuber가 같은 경우 무조건 1
    if N == number:
        return 1

    #set을 list의 형태로 관리한다
    #list[i]는 n을 i개 사용해서 만든 숫자의 모음들
    #최대 7까지만 확인하므로 리스트의 크기는 8(0은 사용 안함)
    s = [set() for i in range(8)]

    #각각의 set에 N,NN,NNN...을 추가
    for i, x in enumerate(s, start=1):
        x.add(int(str(N) * i))

    #각 원소의 사칙 연산을 진행 및 대입
    for i in range(1, 8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)

        #해당 set에 number가 있는지 확인
        #원하는 값이 존재한다면 다음 연산을 종료
        if number in s[i]:
            answer = i + 1
            break

    #7번 내에 원하는 값을 못찾으면  -1 반환
    else:
        answer = -1
    return answer