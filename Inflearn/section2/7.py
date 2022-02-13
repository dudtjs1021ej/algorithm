# 자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요. 
# 만약 20이 입력되면 1부터 20까지의 소수는 2, 3, 5, 7, 11, 13, 17, 19로 총 8개입니다. 
# 제한시간은 1초입니다.

import sys
def mySolution():
    n = int(input())
    if n < 2:
        count = 0
    else: # 2 이상이면 소수에 2포함해서 시작
        count = 1

    for i in range(3,n+1):
        for j in range(2,i):  
            if (i % j == 0):
                break

            if i-1 == j:
                count += 1
    print(count)

# 에라토스테네스 체
def answer():
    n = int(input())
    ch = [0]*(n+1) # 다 0으로 초기화
    count = 0
    for i in range(2,n+1):
        if ch[i] == 0:
            count += 1
            for j in range(i,n+1,i): # i의 배수는 모두 소수에서 제외
                ch[j] = 1
    print(count)

answer()

# 후기
# 소수를 구할 때, 배수를 제외하며 구하는 방법은 생각하지 못함 (ex) i가 2이면 4,6,8 .. 제외)
                 
        
    
   
        
