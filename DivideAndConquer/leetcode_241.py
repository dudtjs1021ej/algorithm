from typing import List
# 괄호를 삽입하는 여러가지 방법 

class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r))) # string으로 합치고 eval로 연산
            return results

        if input.isdigit():
            return [int(input)]

        results = []
        for index, value in enumerate(input):
            if value in "-+*": # 연산자를 기준으로 왼/오 분할
                left = self.diffWaysToCompute(input[:index])
                right = self.diffWaysToCompute(input[index + 1:])

                results.extend(compute(left, right, value)) # 계산한 값 extend
        return results