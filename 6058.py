'''
문제 - 기초-논리연산
코드업 6058 참/거짓이 서로 같을 때에만 참 출력하기
https://codeup.kr/problem.php?id=6058
'''


a, b = map(int, input().split())
print(bool(a) == False and bool(b) == False)
