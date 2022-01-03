골드바흐 추측은  "2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다." 대충 이런뜻이고
이해하기 쉬운 문제임에 반해 아직도 증명되지 않았다고 한다ㄷㄷ


pnum = [x for x in range(2,10001) if x == 2 or x % 2 == 1]
for j in range(3,100,2):
    for i in range(2*j,10001,j):
        if i in pnum:
            pnum.remove(i)

a = int(input())
for x in range(a):
    n = int(input())
    for y in range(n//2,1,-1):
        if y in pnum and n-y in pnum:
            print(y,n-y)
            break

윗줄은 전에 썼던 구간별 소수 구하기를 그대로 가져왔고
밑에줄은 인풋값의 중간서부터 1씩 빼가면서 가장 큰 소수를 구하기로 했다
예를 들어서 input이 16이면 8부터 7,6,5 ... 순서로 빼가는것
그럼 7,9 6,10 5,11 이런 순서로 숫자가 나타나는데  5,11은 둘다 소수니까... 너무 주저리주저리 써놨네
