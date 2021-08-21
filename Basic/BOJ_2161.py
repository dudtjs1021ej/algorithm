import sys

def deleteCard(cardList):
    while True:
        if len(cardList) == 1:
            print(cardList[0], end=" ")
            break

        print(cardList.pop(0), end=" ") # 앞장 버림
        cardList.append(cardList.pop(0)) #버린 다음 장 맨 뒤로 보냄

N = int(sys.stdin.readline())
cardList = []

for i in range(1,N+1):
    cardList.append(i)

deleteCard(cardList)


