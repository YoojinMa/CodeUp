'''
문제 - 기초-종합
코드업 6077 짝수 합 구하기
https://codeup.kr/problem.php?id=6077
'''


a = int(input())
t = 0
for i in range(1, a+1):
    if i % 2 == 0:
        t += i

print(t)
