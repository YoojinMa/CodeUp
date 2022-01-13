'''
문제 - 기초-종합
코드업 6086 거기까지! 이제 그만~
https://codeup.kr/problem.php?id=6086
'''


n = int(input())
s = 0
c = 0

while True:
    s += c
    c += 1
    if s >= n:
        break

print(s)
