n,m = list(map(int,input().split()))
l = []

def bcktrck(a):
    if len(l) == m:
        a = list(map(str,l))
        print(' '.join(a))
        
    else:
        for j in range(a,n+1):
            if j not in l:
                l.append(j) 
                bcktrck(j+1) #j를 써서 앞자리보다 작은 수가 뒤에 나오지 않게 해준다
                l.pop() 

bcktrck(1)

리스트에 추가해서 걸러볼까 하다가 어제 메모리초과로 호되게 혼난 나는 열심히 머리를 굴리고 있었다
하지만 생각이 나지 않았다...

https://jiwon-coding.tistory.com/22 님의 코드를 참고했다
  
다행히? 15649코드가 같아서..문제를 푸는데 수월했지만
아직 난 저정도로 생각을 하지 못한다는게 아쉽다.
백준을 잠깐 쉬고 알고리즘 공부를 해볼까 하는데 음
