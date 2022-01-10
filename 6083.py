'''
문제 - 기초-종합
코드업 6083 빛 섞어 색 만들기
https://codeup.kr/problem.php?id=6083
'''


r, g, b = map(int, input().split())

for i in range (0, r):
    for j in range (0, g):
        for k in range (0, b):
            print(i, j, k)

print(r * g * b)
