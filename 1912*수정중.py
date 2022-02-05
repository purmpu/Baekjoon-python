#이 파일을 마지막으로 백준 중단

import sys
n = int(sys.stdin.readline())

l = list((map(int,sys.stdin.readline().split())))

plus = sum(l)

r = []
for i in range(n):
    for j in range(n):
        if sum(l[i:j+1]) > plus:
            r.append(sum(l[i:j+1]))
        
print(r)

#-1-2-3-4-5일때 0나오는 이유 찾기

i와j가 같을때 0이 append되는것 같은데 하아
