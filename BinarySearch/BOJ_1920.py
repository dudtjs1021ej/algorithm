import sys

# 방법 1 - 재귀사용x
def binary_search(n, numberList):
   # numberList.sort() 
    startIndex = 0
    endIndex = len(numberList) - 1

    while(startIndex <= endIndex):
        midIndex = (startIndex + endIndex) // 2 #몫만 나오게(소수점버림) //연산자 사용
        
        if numberList[midIndex] == n: #찾는 숫자가 있으면 리턴 1
            return 1

        elif numberList[midIndex] < n:
            startIndex = midIndex + 1     

        else:
            endIndex = midIndex - 1

    return 0 #없으면 리턴 0

#방법2 - 재귀 사용o
def binary_search(n, NList, startIndex, endIndex):
    if startIndex > endIndex:
        return 0
    midIndex = (startIndex + endIndex) // 2
    if NList[midIndex] == n :
        return 1
    elif NList[midIndex] < n :
        return binary_search(n, NList, midIndex+1, endIndex)
    else:
        return binary_search(n, NList, startIndex, midIndex - 1)


N = int(sys.stdin.readline()) 
NList = sorted(map(int, sys.stdin.readline().split())) #정렬된 상태로 받음
M = int(sys.stdin.readline()) 
MList = list(map(int, sys.stdin.readline().split()))

for i in MList:
    startIndex = 0
    endIndex = len(NList) - 1
    print(binary_search(i, NList))
    
