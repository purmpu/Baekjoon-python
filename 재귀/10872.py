a = int(input())
b = 1
for c in range(a,1,-1):
    b = c*b
print(b)

팩토리얼을 구하는 문제이다

1*2*3*...*n 으로 계산 해도 되겠지만 여러가지 유튜브나 위키 문제해설등을 찾아보면 항상 n*n-1*n-2..식으로 풀길래 나름 따라해보았다.
아마 팩토리얼의 정의는 n부터 1까지 1씩 감소하며 곱하는 것 인가부다

다음 코드는 재귀함수로 푼 코드이다

def fac(n):
    if n == 0:
        return 1
    else:
        r = n*fac(n-1)
    return r
n = int(input())
print(fac(n))    

#for문보다 재귀함수를 쓰는 방법이  n*n-1*n-2... 방식을 나타내기에 더 적합한것 같다
