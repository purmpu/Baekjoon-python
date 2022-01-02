l = []
l2= []
for _ in range(3):
    a,b = map(int,input().split())
    if a in l:
        l.remove(a)
    else:
        l.append(a)
    if b in l2:
        l2.remove(b)
    else:
        l2.append(b)
print(l[0],l2[0])

처음에 조금 고민했었는데 아마 초콜릿이 부족해서 그랬던것 같다

사각형을 이루는 네 점에는 공통점?이 있는데 x1이 두개, x2가 두개. y1이 두개, y2가 두개.
구래서 이중에 개수가 2개가 아닌 x나y를 찾으면 되는 간단한 문제이다.
하지만 실력이 부족한 나는 찾는 방법을 아무리 생각해도 구현 할 수가 없어서 그냥 남기는 방법을 쓰기로 했다 흗흑
