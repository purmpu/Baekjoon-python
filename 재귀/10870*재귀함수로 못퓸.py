a = int(input())
l = [0,1]
b =0 
c =1
for _ in range(a):
    c = b + c
    b = c - b
    l.append(c)
print(l[a])

피보나치수열인데 딱히 설명할건 없는것같다


재귀함수를 이해를 못하겠ㄷ가 대체
