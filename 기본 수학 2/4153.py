while True:
    l = list(map(int,input().split()))
    if sum(l) == 0:
        break
    a = sorted(l)
    if a[0]**2 + a[1]**2 == a[2]**2:
        print("right")
    else:
        print("wrong")

삼각형이 직각인지 아닌지를 구하려면 세 변 a,b,c가 
a^2 + b^2 = c^2    라는 공식에 맞아야 한다.
간단히 피타고라스를 쓰면 되는 문제인데 무조건 작은 순서로 인풋이 들어가는게 아니라는것을 간과하여서 
뭐가 문제일까? 히며 5번을 틀렸다
결국 sorted를 추가하고 끝낫다
