#!/usr/bin/python3
from collections import Counter

input_counter = Counter(input().upper()) #대문자로 입력받고, 문자 수
mc_results = input_counter.most_common(2) #튜플을 가진 리스트로 반환

if len(mc_results) == 1:        #한 문자만 입력받았을 경우
    print(mc_results[0][0])
    
elif mc_results[0][1] != mc_results[1][1] and len(mc_results) >= 2:
    print(mc_results[0][0].upper())
else:
    print("?")