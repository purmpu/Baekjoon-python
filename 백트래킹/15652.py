n,m = list(map(int,input().split()))
l = []

def bcktrck(a):
    if len(l) == m:
        a = list(map(str,l))
        print(' '.join(a))
        
    else:
        for j in range(a,n+1):
                l.append(j)
                if j >= l[-1]:
                    bcktrck(j)
                l.pop() 

bcktrck(1)

흥 이제 백트래킹 정도야
