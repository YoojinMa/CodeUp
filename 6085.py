'''
문제 - 기초-종합
코드업 6085 그림 파일 저장용량 계산하기
https://codeup.kr/problem.php?id=6085
'''


w, h, b = map(int, input().split())

result = w * h * b / 8 / 1024 / 1024

print(format(result, ".2f") + " MB")
