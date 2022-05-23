def solution(str1, str2):
    from collections import Counter

    #소문자로 변환 후 두 개의 문자가 영문일 경우만 리스트에 담는다
    li1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    li2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    #둘 다 원소가 존재하지 않으면 1(1*65536)
    if len(li1+li2)==0:
        return 65536

    c1 = Counter(li1)
    c2 = Counter(li2)
    uni = sum((c1|c2).values())     #합집합
    inter = sum((c1&c2).values())   #교집합

    return int(inter/uni*65536)