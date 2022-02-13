# 문자열 내장함수
s = "Hi Everyone"
print(s.upper()) # HI EVERYONE -> 대문자 변환
print(s.lower()) # hi everyone -> 소문자 변환
print(s.find('E')) # 3 -> E의 인덱스 리턴
print(s.count('e')) # 2 -> e의 개수 리턴
print(s[:2]) # Hi -> 0,1 인덱스에 해당하는 문자열 리턴
print(s.isupper()) # False -> 모두 대문자인지 True / False 로 출력

# 리스트 내장함수
a = list(range(1, 11)) 
print(a) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a.insert(1,15)
print(a) # [1, 15, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a.pop()) # 10
print(a.pop(0)) # 1
print(a) # [15, 2, 3, 4, 5, 6, 7, 8, 9] -> 다 pop 되어있음
a.remove(4) 
print(a) # [15, 2, 3, 5, 6, 7, 8, 9] -> value 4 자움
print(a.index(5)) # 3
a.sort()
print(a) # [2, 3, 5, 6, 7, 8, 9, 15]
a.clear()
print(a) # []


# 람다 함수 -> 1,2 같은 표현 , 훨씬 구현 간단
b = [1, 2, 3]

# 1
def plus_one(x):
    return x+1
print(list(map(plus_one, b)))

#2 
print(list(map(lambda x: x+1, b)))



