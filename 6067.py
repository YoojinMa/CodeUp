'''
문제 - 기초-조건/선택실행구조
코드업 6067 정수 1개 입력받아 분류하기
https://codeup.kr/problem.php?id=6067
'''


a = int(input())
if (a < 0 and a % 2 == 0):
    print("A")
elif (a < 0 and a % 2 != 0):
    print("B")
elif (a > 0 and a % 2 == 0):
    print("C")
else:
    print("D")
