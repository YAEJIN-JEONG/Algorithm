#https://programmers.co.kr/learn/courses/18/lessons/1878

def solution(v) :
    answer = []
    xlist, ylist=[]
    for x in v:
        xlist.append(x[0])
        ylist.append(x[1])
    for i in xlist:
        if xlist.count(i) == 1:
            dx = i
    for j in ylist:
        if ylist.count(j) == 1:
            dy = j
    answer = [dx,dy]

    return answer