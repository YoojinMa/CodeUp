'''
문제 - 기초-조건/선택실행구조
코드업 6065 정수 3개 입력받아 짝수만 출력하기
https://codeup.kr/problem.php?id=6065
'''


a, b, c = map(int, input().split())
if (a % 2 == 0):
    print(a)
if (b % 2 == 0):
    print(b)
if (c % 2 == 0):
    print(c)
