# 이것이 코딩 테스트다 with Python 나동빈
# 스타벅스 22.8.19 금 17:41

a = [1,4,3]
print("기본 리스트 :",a)

# 리스트에 원소 삽입(맨 마지막 인덱스로 추가)
a.append(2)
print("리스트에 원소 삽입",a)

# 오름차순 정렬
a.sort()    # 시간복잡도 O(NlogN)
print("오름차순 정렬 :",a)

# 내림차순 정렬
a.sort(reverse=True)    # 시간복잡도 O(NlogN)
print("내림차순 정렬 :",a)

# 리스트 원소 순서 뒤집기
a.reverse()
print("원소 순서 뒤집기 :",a)
a.reverse()
print("원소 순서 뒤집기 :",a)

# 특정 인덱스에 데이터 추가
a.insert(2,5) # 시간복잡도 O(N) 여러개 남발하면 컷. 삽입 후 원소 위치 조정해야해서 그럼.
print("인덱스 2에 5 추가",a) # index 2, 세번째 원소 자리에 5추가, 기존 값은 뒤로 밀린다.

# 특정 값인 데이터 개수 세기
print("값이 3인 데이터 개수 :",a.count(3))

# 특정 값 데이터 삭제(여러개면 하나만 삭제)
a.remove(1) # 여러개 남발하면 컷. 시간복잡도 O(N).
print("값이 1인 데이터 삭제 :", a)

# Python은 remove_all()과 같은 함수 제공x
a = [1,2,3,4,5,5,5]
remove_set=[3,5]

result = [ i for i in a if i not in remove_set]
print(result)



