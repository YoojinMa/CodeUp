'''
문제 - 기초-종합
코드업 6081 16진수 구구단 출력하기
https://codeup.kr/problem.php?id=6081
'''


n = int(input(), 16)
F = int('F', 16)

for i in range (1, F+1):
    print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')
