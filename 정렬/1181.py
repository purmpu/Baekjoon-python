n = int(input())
l = []
l1 = []
for _ in range(n):
    l.append(input())
l = set(l)
for i in l:
    l1.append([len(i),i])
l1 = sorted(l1)
for i in range(len(l1)):
    print(l1[i][1])
    
    
    
처음에 len을 이용하여 풀려고 했는데 그게 안돼서 머리굴리다가 구글링을 해봤다

https://wook-2124.tistory.com/468 님의 코드를 참고하였다
  
리스트 요소의 len값을 같이 넣어서 푸신걸 보고 그걸 중심으로 내 코드를 짜봤다
천재이신것같다
