'''
문제 - 기초-3항연산
코드업 6064 정수 3개 입력받아 가장 작은 값 출력하기
https://codeup.kr/problem.php?id=6064
'''


a, b, c = map(int, input().split())
print((a if a < b else b) if ((a if a < b else b) < c) else c)
