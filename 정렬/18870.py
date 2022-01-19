시간초과만 8번... ㅋㅋㅋㅋㅋㅋㅋ

import sys
n = sys.stdin.readline()
l = list(map(int,sys.stdin.readline().split()))
s = sorted(set(l))
d = {s[i]: i for i in range(len(s))}
for i in l:
    print(d[i],end = ' ')
    
구글링해보니 답은 딕셔너리인걸 알았음

전에 제출했던 시간초과 코드는 아래
어떻게든 시간을 줄이려 한 노력이 sys에서 보인다!!

import sys
n = sys.stdin.readline()
l = list(map(int,sys.stdin.readline().split()))
s = set(l)
for i in l:
    count = 0
    for k in s:
        if i > k:
            count += 1
    print(count,end=' ')
    
    
  
