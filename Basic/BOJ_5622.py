import sys
alphabet = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
s = list(sys.stdin.readline())
result = 0
for i in s:
    for j in alphabet:
        if i in j:
            result += alphabet.index(j) + 3
       
print(result)