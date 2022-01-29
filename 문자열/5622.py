n = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

N = input()
l = []
for i in n:
    for j in i:
        for k in N:
            if k == j:
                l.append(n.index(i)+3)

print(sum(l))



for문이 3번... for문이..3번...
