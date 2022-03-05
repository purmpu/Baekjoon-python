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

2022 03 05 블로그 쓰다가 더 짧게품

x,y,w,h = map(int,input().split())
l = [w-x,h-y,x,y]
a = sorted(l)
print(a[0])

근데 메모리랑 시간이 더 늘어났다 왜지

2022 03 05 아 이게 더 짧게 되네

x,y,w,h = map(int,input().split())
l = [w-x,h-y,x,y]
print(sorted(l)[0])
