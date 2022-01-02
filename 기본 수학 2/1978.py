N = int(input())
num = map(int,input().split())
count = 0
for i in num:
    ic = 0
    if i == 1:
        ic += 1
    for k in range(2,i):
        if i % k == 0:
            ic += 1
    if ic == 0:
        count += 1
print(count)
