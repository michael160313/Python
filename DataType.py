# 이것이 코딩 테스트다 with Python 나동빈 22.8.19
a = 0.3 + 0.6
print(a)    # 0.8999999가 나온다.
print(round(a,4)) # 반올림해서 0.9가 나온다. 

if round(a,4) == 0.9:
    print(True)
else:
    print(False)


# 나누기 / , 나머지 %, 나눈 몫  //

c = 7
d = 3

print(c/d) # Python은 기본적으로 나누기 연산자 사용하면 결과값을 실수형으로 처리한다. 2.333333~
print(c%d) # 1 나머지
print(c//d) # 2 몫

# 거듭제곱 연산자 **
print(c ** d) # 결과값 343

