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

피곤하니 다음에 수정함
