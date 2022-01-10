N = int(input())
l = []
for _ in range(N):
    l.append(list(map(int,input().split())))

for a in range(0,len(l)):
    s = 1
    for b in range(0,len(l)):
        if l[a][0] < l[b][0] and l[a][1] < l[b][1]:
            s = s + 1
    print(s,end = ' ')
