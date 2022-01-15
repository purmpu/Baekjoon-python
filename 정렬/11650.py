n = int(input())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
l = sorted(l)
for a in l:
    print(a[0],a[1])
    
  
  으음 [1,-1] [2,4] 이런거에 sorted가 가능할줄은 몰랐다
