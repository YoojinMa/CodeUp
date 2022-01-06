'''
문제 - 기초-종합
코드업 6079 언제까지 더해야 할까?
https://codeup.kr/problem.php?id=6079
'''


a = int(input())
t = 0
    
for i in range(0, a):
    i += 1
    t += i
    
    if (t >= a):
        print(i)
        break
