n = int(input())
result = 0
for _ in range(n):
    wrd = input()
    plus = 0
    for j in wrd:
        num = wrd.count(j)
        ind = wrd.index(j)
        lis = wrd[ind:ind+num]
        if lis.count(j) == len(lis):
                plus += 1
    if plus == len(wrd):
        result += 1
print(result)

이제 요정도는 아무것도 안찾아보고 그냥 풀수 있게됐다
아직 갈길이 멀다 홧팅!!
