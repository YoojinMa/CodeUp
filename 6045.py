'''
문제 - 기초-산술연산
코드업 6045 정수 3개 입력받아 합과 평균 출력하기
https://codeup.kr/problem.php?id=6045
'''


a, b, c = map(int, input().split())
n = a + b + c
print(n, format(n / 3, ".2f"))
