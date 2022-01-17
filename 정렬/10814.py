n = int(input())
l = []
l1 = []
for _ in range(n):
    a,b = input().split()
    l.append([int(a),len(l),b])
l = sorted(l)
for i in range(len(l)):
    print(l[i][0],l[i][2])
    
    
1181과 같은 방법으로 풀었다. 나이,이름 사이에 len(리스트)를 넣어서 sort를 할때 나이로 한번 정렬, 리스트 들어온 순서로 한번 더 정렬하게 해줬다
푸는데 10분걸린 나 칭찬해~
