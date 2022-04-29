import sys
#n,m
n,m = sys.stdin.readline().strip().split()
#이름|순서가 키인 딕셔너리(일반 리스트는 시간 초과 발생)
liKey={}
liName={}

#포켓몬을 입력받음
for i in range(int(n)):
    a=sys.stdin.readline().strip()
    liKey[i]=a
    liName[a]=i

#포켓몬 검색
for i in range(int(m)):
    a = input()
    if a.isalpha():#이름으로 검색시
        print(liName[a]+1)
    if a.isdigit():#도감번호로 검색시
        print(liKey[int(a)-1])