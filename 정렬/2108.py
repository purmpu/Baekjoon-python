from collections import Counter
import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))

def mean(l): #평균
    if len(l) == 1:
        return l[0]
    else:
        return round(sum(l) / n)

def median(l): #중간
    if len(l) == 1:
        return l[0]
    else:
        return l[(len(l)) // 2]

def mode(l): #최빈
    m = Counter(l).most_common(2)
    if len(l) == 1:
        return l[0]
    elif m[0][1] == m[1][1]:
        return m[1][0]
    else:
        return m[0][0]

def rrange(l): #범위
    if len(l) == 1:
        return 0
    else:
        return l[-1] - l[0]

l = sorted(l)
print(mean(l))
print(median(l))
print(mode(l))
print(rrange(l))


와우... 여기서 sys의 위력을 다시한번 체감했습니다
