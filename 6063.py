'''
문제 - 기초-3항연산
코드업 6063 정수 2개 입력받아 큰 값 출력하기
https://codeup.kr/problem.php?id=6063
'''


a, b = map(int, input().split())
print(a if (a>=b) else b)
