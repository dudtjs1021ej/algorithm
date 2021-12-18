import sys
from typing import Collection
# J는 보석, S는 돌이다. S에 있는 보석의 개수를 출력
# J = "aA" S = "aAAbbb" -> 3 출력

# 1. 해시 테이블로 풀이
class Solution:
    def numJewelsInStones1(self, J: str, S: str) -> int:
        freqs = {}
        count = 0
        
        for char in S:
            if char in freqs: 
                freqs[char] = 1 # freqs에 처음 들어오는 돌이면 빈도수 1
            
            else:
                freqs[char] += 1 # freqs에 있던 돌이면 빈도수+1
                
        for char in J:
            if char in freqs:
                count += freqs[char] #보석에 해당하는 빈도수를 count에 더함
                
        return count

# 2. defaultdict로 비교 생략
    def numJewelsInStones2(self, J: str, S: str) -> int:
        freqs = Collection.defaultdict(int) # 존재하지 않는 키에 대해 디폴트를 리턴 -> 값이 없으면 0
        count = 0
        
        for char in S:
            freqs[char] += 1 # 비교없이 돌의 빈도수 계산
        
                
        for char in J:
            count += freqs[char] #비교없이 보석 빈도수 계산
                
        return count

# 3. Counter로 계산 생략
    def numJewelsInStones3(self, J: str, S: str) -> int:
        freqs = Collection.Counter(S)
        count = 0
                
        for char in J:
            count += freqs[char] 
                
        return count