# Anagram이란 두 문자열이 알파벳의 나열 순서를 다르지만 
# 그 구성이 일치하면 두 단어는 아나그램이라고 합니다.
import sys
a = input()
b = input()
str1 = dict()
str2 = dict()
for x in a:
    str1[x] = str1.get(x, 0) + 1 # 존재하면 x의 value불러오고 없으면 0
for x in b:
    str2[x] = str2.get(x, 0) + 1

for i in str1.keys(): 
    if i in str2.keys(): # 둘 다 같은 키값이 있다면
        if str1[i] != str2[i]:
            print("NO")
            break
    else:
        print("NO")
        break
else:
    print("YES")


# dict1 = dict()
# dict2 = dict()
# a = input()
# b = input()
# for x in a:
#     if x in dict1:
#         dict1[x] += 1
#     else:
#         dict1[x] = 1 

# for x in b:
#     if x in dict1:
#         dict1[x] -= 1
#     else:
#         dict1[x] = 1 

# for key, value in dict1.items():
#     if value != 0:
#         print("NO")
#         break
# else:
#     print("YES")

# 후기
# 내가 푼게 나은듯하다.
# 딕셔너리에 key는 문자, value엔 개수를 넣고 
# a는 개수를 +1, b는 개수를 -1해서 value가 모두 0이면 애너그램 판별하게 풀이
