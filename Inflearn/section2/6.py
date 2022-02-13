# N개의 자연수가 입력되면 각 자연수의 자릿수의 합을 구하고, 
# 그 합이 최대인 자연수를 출력 하는 프로그램을 작성하세요. 
# 각 자연수의 자릿수의 합을 구하는 함수를 def digit_sum(x)를 꼭 작성해서 프로그래밍 하세요.

import sys

def mySolution():
    # 문자열로 받고 각 문자마다 int형으로 변환해서 합함
    def digit_sum(num):
        sum = 0
        for s in num:
            sum += int(s)
        return sum

    n = int(input())
    num_list = list(input().split())
    max = -2147000000

    for num in num_list:
        sum = digit_sum(num)
        if max < sum:
            max_num = num
            max = sum

    print(num)

def answer():
    # 첫 번째 방법 - 10으로 나눈 나머지로 각 자리수의 합 구함
    def digit_sum1(x):
        sum = 0
        while x>0:
            sum += x%10
            x = x//10
        return sum

    # 두 번째 방법 - str -> int바꾸면서 합 구함
    def digit_sum2(x):
        sum = 0
        for s in str(x):
            sum += int(s)
        return sum

    n = int(input())
    num_list = list(map(int, input().split()))
    max = -2147000000

    for num in num_list:
        sum = digit_sum1(num)
        if max < sum:
            max_num = num
            max = sum
    print(num)

# 후기
# 처음으로 정답과 똑같이 풀었다.
    