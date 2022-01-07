x,y,w,h = map(int,input().split())
l = []
l.append(w-x)
l.append(h-y)
l.append(x)
l.append(y)
a = sorted(l)
print(a[0])

더 짧게 할수도 있겠지만 그냥 통과했으니 올림
0,0과 w,h까지의 거리중 가장 짧은 값만 구하면 되는 문제
