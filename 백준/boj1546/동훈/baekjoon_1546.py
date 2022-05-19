#!/usr/bin/python3
number_list  = int(input()) #시험 본 과목의 개수
grade_list = list(map(int, input().split()))

denominator = max(grade_list)
grade  = 0
average_grade = 0
for i in range(number_list):
    grade += grade_list[i]/denominator

print ((grade/number_list) * 100)