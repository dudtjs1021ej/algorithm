import sys
# 매일 화씨 온도 리스트 T를 입력받아서 더 따뜻하 날씨를 위해서는 며칠을 더 기다려야 하는지 출력
def dailyTemperatures(self, T):
    answer = [0] * len(T)
    stack = []
    for i, cur in enumerate(T):
        
        while stack and cur > T[stack[-1]]:
            last = stack.pop()
            answer[last] = i - last
        stack.append(i)

    return answer