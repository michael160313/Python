# 이것이 코딩 테스트다 , 문자열 , 22.8.19 18시 스타벅스

# " ", ' '로 문자열 초기화. \" \", \' \'처럼 문자열에 포함 가능.
data = 'Hello World'
print(data)

# " ' ' ", ' " " ' 가능.
data = "Don't you know 'Python'?"
print(data)

data = 'Don\'t you know "Python"?'
print(data)

# 문자열 연산은 +
a = "Hello"
b = 'World'
print(a+" "+b)

# 문자열 변수를 양의 정수와 곱하면 그 값만큼 반복.
print(a * 2)

# Python의 문자열은 내부적으로 리스트로 처리. 즉, 인덱싱과 슬라이싱 가능.
a='ABCDEF'
print(a[1:4]) # 인덱스1부터 4-1(3)까지 출력, 두번째부터 네번째 원소까지 출력.
