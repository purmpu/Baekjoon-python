N = int(input())
RN = N
count = 0
l = []
while N >= 0:
    if N % 5 == 0:
        l.append(N / 5 + count)
    elif N % 3 == 0:
        l.append(N / 3 + count)
    N -= 5
    count += 1
if len(l) == 0:
    print(-1)
else:
    print(int(l[-1]))
