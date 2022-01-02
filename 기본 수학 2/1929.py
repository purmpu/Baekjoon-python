m,n = map(int,input().split()) #인풋 받기

a = [False,False] + [True]*(n-1) #에라토스테네스의 체
primes=[]

for i in range(2,n+1):
  if a[i]:
    primes.append(i)
    for j in range(2*i, n+1, i):
        a[j] = False
for v in range(len(primes)): #위 코드는 n까지의 소수를 모두 구하므로 m의 조건을 달아줘야함
    if primes[v] >= m:
        print(primes[v])
