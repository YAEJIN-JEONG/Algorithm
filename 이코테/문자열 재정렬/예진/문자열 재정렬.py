data = input()
result = []
value = 0

#문자 하나씩 확인
for x in data:
    #알파벳인 경우 확인 .isalpha()
    if x.isalpha():
        result.append(x)
    else:
        value +=int(x)

#알파벳 정렬
result.sort()

#숫자가 존재하는지 확인 후 뒤에 append
if value != 0 :
    result.append(str(value))

#리스트를 문자열로 변환하여 출력 ''.join()
print(''.join(result))