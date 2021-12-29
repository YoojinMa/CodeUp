'''
문제 - 기초-반복실행구조
코드업 6074 문자 1개 입력받아 알파벳 출력하기
https://codeup.kr/problem.php?id=6074
'''


a = ord(input())
ch = ord('a')
while (a >= ch):
    print(chr(ch), end = ' ')
    ch += 1
