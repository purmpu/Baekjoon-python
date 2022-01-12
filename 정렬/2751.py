sys를 이용했다.
2750의 코드를 그대로 복사해서 제출해봤는데 시간초과가 떴다
아마 수의 범위가 100만까지 늘어나서 인듯
input과 print가 느릴때 sys를 쓰는걸 몇번 보긴 했는데 정작 써본적은 없어서 이참에 써봤다
기본적인 코드는 2750과 같다

import sys

n = int(input())
l = []
for b in range(n):
    l.append(int(sys.stdin.readline()))
l = sorted(l)
for a in l:
    sys.stdout.write(str(a) + '\n')
    
sys.stdin.readline 은 input보다 메모리는 크게 사용하지만 속도는 그만큼 빠르다고 한다..신기한 파이썬 세상

 sys.stdout.write(str(a) + '\n') 
 여기서 + '\n'을 쓴 이유는 sys.stdout.write(str(a))로 출력시에 줄바꿈처리가 없이 출력되기 때문이다 귀찮게군다
