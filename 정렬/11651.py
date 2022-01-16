import sys
n = sys.stdin.readline()
l = []
for _ in range(int(n)):
    x,y = map(int,sys.stdin.readline().split())
    l.append([y,x])
l = sorted(l)
for a in l:
    print(a[1],a[0])
    
    
11650과 98% 일치하는 코드다
그냥 sort의 기준을 y좌표로만 바꿔줬다
