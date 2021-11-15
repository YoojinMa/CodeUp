'''
문제 - 기초-논리연산
코드업 6055 하나라도 참이면 참 출력하기
https://codeup.kr/problem.php?id=6055
'''


a, b = map(int, input().split())
print(bool(a) or bool(b))
