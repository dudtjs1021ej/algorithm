# N개의 자연수가 입력되면 각 자연수를 뒤집은 후 그 뒤집은 수가 소수이면 그 수를 출력하는 프로그램을 작성하세요. 
# 예를 들어 32를 뒤집으면 23이고, 23은 소수이다. 
# 그러면 23을 출력 한다. 단 910를 뒤집으면 19로 숫자화 해야 한다. 
# 첫 자리부터의 연속된 0은 무시한다.
# 뒤집는 함수인 def reverse(x) 와 소수인지를 확인하는 함수 def isPrime(x)를 반드시 작성하 여 프로그래밍 한다.
import sys

def mySolution():
    def reverse(x):
        return int(x[::-1]) # 문자열로 역순시킨후 int형으로 변환

    def isPrime(x):
        for i in range(2,x): # 1은 모두 나눠지기 때문에 2부터 시작 ~ x-1까지 체크
            if x % i == 0:
                return False      
        return True

    n = int(input())
    n_list = list(input().split())
    for i in n_list:
        reverse_i = reverse(i)
        if (isPrime(reverse_i)):
            print(reverse_i, end=' ')

def answer():
    # 10으로 나눈 나머지를 res에 자리수에 맞게 더해감
    def reverse(x):
        res = 0
        while x>0:
            t = x%10
            res = 10*res + t
            x = x//10
        return res

    def isPrime(x):
        if x==1:
            return False
        for i in range(2,x//2 + 1): # 16이면 2*8이기때문에 8까지만 따져보면 됨
            if x % i == 0:
                return False

        return True
    
    n = int(input())
    a = list(map(int,input().split()))
    for x in a:
        tmp = reverse(x)
        if isPrime(tmp):
            print(tmp, end= ' ')

answer()

# 후기
'''
잘못 푼 점
1. 소수 체크할 때, 1인 경우 안따졌다,,
2. 문자열 뒤집기로 꼼수로 풀었다.

새로 배운 것
약수는 절반까지만 체크 해도 된다.
'''



