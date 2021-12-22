M = int(input())
N = int(input())
li2 = []
for i in range(M,N+1):
    ic = 0
    if i == 1:
        ic += 1
    for k in range(2,i):
        if i % k == 0:
            ic += 1
            break
    if ic == 0:
        li2 += [i]
if len(li2) == 0:
    print(-1)
else:
    print(sum(li2))
    print(min(li2))
