'''
문제 - 기초-종합
코드업 6084 소리 파일 저장용량 계산하기
https://codeup.kr/problem.php?id=6084
'''


h, b, c, s = map(int, input().split())

result = h * b * c * s / 8 / 1024 / 1024

print(format(result, ".1f") + " MB")
