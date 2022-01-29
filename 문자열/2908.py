A,B = input().split()
A = int(A[::-1])
B = int(B[::-1])

if A > B:
    print(A)
else:
    print(B)
    
    
[::-1]이 역순으로 바꾼다는 뜻이다
[]이 있는걸 보면 슬라이싱인데 리스트가 아닌 문자열에도 쓸 수 있다는게 참 좋은것 같다
reverse를 써봤는데 str이라고 오류가 났다
