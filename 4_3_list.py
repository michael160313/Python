students = ["egoing", "sori", "maru"] # 0,1,2번지 원소 list 이름 students
grades = [2, 1, 4]
print('students[1]',students[1]) # 1번지 원소 출력
print('len(students)',len(students)) # students list가 원소 몇개 가지고 있는지 길이 출력
print('min(grades)',min(grades)) # min 최소값
print('max(grades)',max(grades)) # max 최대값
print('sum(grades)',sum(grades)) # 총합

import statistics # 통계 모듈 statistics import
print('statistics.mean(grades)',statistics.mean(grades)) # 평균값 출력

import random # random 모듈 import
print('random.choice(students)',random.choice(students)) # random으로 students list 원소 출력

