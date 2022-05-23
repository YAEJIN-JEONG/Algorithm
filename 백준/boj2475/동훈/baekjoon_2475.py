#!/usr/bin/python3

############# 백준 2475  검증수 문제 #############

serial_number = list(map(int, input().split()))    #정수 입력 및 리스트화

serial_number = list(map(lambda x : x*x , serial_number))  #배열 값 각 수의 제곱 

match_number = sum(serial_number) % 10

print(match_number)