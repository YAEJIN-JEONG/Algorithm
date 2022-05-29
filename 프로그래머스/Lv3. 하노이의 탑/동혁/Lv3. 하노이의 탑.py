answer = []
def solution(n):
    ha(n,1,2,3)
    return answer

#재귀식으로 구현
#공식 참조
def ha(n,a,b,c):
    if n==1:
        answer.append([a,c])
    else:
        ha(n-1,a,c,b)
        answer.append([a,c])
        ha(n-1,b,a,c)