'''
문제 - 기초-종합
코드업 6082 3 6 9 게임의 왕이 되자
https://codeup.kr/problem.php?id=6082
'''


n = int(input())

for i in range (1, n+1):
    if i % 10 == 3:
        print("X", end = ' ')
    elif i % 10 == 6:
        print("X", end = ' ')
    elif i % 10 == 9:
        print("X", end = ' ')
    else:
        print(i, end = ' ')
