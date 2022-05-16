#!/usr/bin/python3

#****************boj 1330******************

# input_list = input().split()

# if input_list[0] > input_list[1]:
#     print('>')
# elif input_list[0] < input_list[1]:
#     print('<')
# else:
#     print('==')


A,B = map(int,input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')
