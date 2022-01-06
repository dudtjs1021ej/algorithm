# t가 s의 애너그램(재배열해도 같은 문자열) 인지 판별하라.

def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)