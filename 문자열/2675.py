n = int(input())
for i in range(n):
    a,b = input().split()
    c = ''
    for i in b:
        c += int(a)*i
    print(c)
    
어이없게 틀렸다 위에게 맞는코드고 아래가 틀린 코드다


n = int(input())
c = ''
for i in range(n):
    a,b = input().split()
    for i in b:
        c += int(a)*i
    print(c)
    
c를 포문 밖에다 정의해놔서 c값이 계에에속 쌓였다
