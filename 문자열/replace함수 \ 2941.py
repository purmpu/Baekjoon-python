n = input()

wrd = ['c=','c-','dz=','d-','lj','nj','s=','z=']

c = 0

for i in range(len(n)):
    if n[i-2]+n[i-1]+n[i] in wrd:
        c += 1
    elif n[i-1]+n[i] in wrd:
        c += 1
    elif n[i-2]+n[i-1]+n[i] and n[i-1]+n[i] not in wrd:
        if i == 0:
            c += 0
        else:
            c += 1

#ljes=njak
print(c)
#print(n[1]+n[2])

처음에 이렇게 저렇게 풀어보려고 위처럼 노가다 하다가 너무 안풀려서 검색을 해봤는데 replace라는 엄청난 함수를 발견했다

n = input()

wrd = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in wrd:
    n = n.replace(i,'*')

print(len(n))

이건 코든데 솔직히 이렇게 짧을 줄은 몰랐다
파이썬에 함수가 너무 많은것 같다 역시
