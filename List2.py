# 이것이 코딩테스트다 with Python 나동빈
# 22.8.19 금 17:27 스타벅스

# 리스트 컴프리헨션을 사용하여 리스트를 초기화
# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
array = [i for i in range(20) if i % 2 == 1]
print(array)

# 위 코드는 아래와 결과가 같다.
array = []
for i in range(20):
    if i % 2 == 1:
        array.append(i)
print(array)

# 1부터 9까지의 수의 제곲 값을 포함하는 리스트
array = [ i * i for i in range(1,10)]
print(array)

# N x M 크기의 2차원 리스트 초기화(리스트 컴프리헨션)
n=3
m=4
array = [[0] * m for _ in range(n)]
print(array)
