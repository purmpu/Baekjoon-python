n,m = list(map(int,input().split()))
l = []

def bcktrck(n,m):
    if len(l) == m:
        a = list(map(str,l))
        print(' '.join(a))
        
    else:
        for j in range(1,n+1):
            if j not in l:
                l.append(j)
                bcktrck(n,m)
                l.pop() #remove는 안돼

bcktrck(n,m)


https://jiwon-coding.tistory.com/21 이분의 블로그를 참고했다..기보다는 완전히 똑같다

다른 블로그를 아무리 읽어봐도 이해가 되지를 않았는데 저분 블로그를 보고 단번에 이해했다

갈 길이 멀다
