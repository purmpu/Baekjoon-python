15649~15651번은 백트래킹을 이해했는가 확인하는 문제같다
if not in j만 지워주면 될것같아서 15650에서 그 줄만 지우고 재귀함수의 bcktrck(a+1)을 a로 바꿔줬다

n,m = list(map(int,input().split()))
l = []

def bcktrck(a):
    if len(l) == m:
        a = list(map(str,l))
        print(' '.join(a))
        
    else:
        for j in range(a,n+1):
                l.append(j)
                bcktrck(a)
                l.pop() 

bcktrck(1)
