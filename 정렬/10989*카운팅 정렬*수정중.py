#input으로 예제data를 넣었다는 가정 하에 설명하는중
#예제 data[5 2 3 1 4 2 3 5 1 7]
def Counting(data,count,result):
    for i in data:
        count[i] += 1
    #count가 [0,0,...data의 길이만큼의 0]인데 각 순서에 맞는 숫자들의 수를 기록하는 문장
    #여기서 count는 [0,2,2,2,1,2,0,1]가 됨
    #print(count)
    for i in range(len(count)-1): #이건 누적count를 세는건데 누적된 수대로 적어야 result칸에 알맞게 쓸 수 있음, 정확히 알아본게 아니라 문제풀다가 혼자 알게된 뇌피셜이라 다음에 더 자세히 알아바야댐
        count[i+1] += count[i]
        #이제 카운트는 누적되서 [0,2,4,6,7,9,9,10] 요렇게 변했을거
    #print('누적',count)
    for i in range(len(data)-1,-1,-1): #data의 맨 마지막부터 처음까지 내려오는 순서로 카운팅함
        result[count[data[i]]-1] = data[i] #count에서의 i의 개수를 적은 위치를 인덱싱해서 다시 result에 그 값을 넣으면 data[i]가 들어갈 자리가 나옴
        count[data[i]] -= 1 #7을 한번 사용했으니 누적count에서 빼주는거임. 근데 왜 빼는지는 잘 몰르겟슴;; 가만냅둬도 상관 없는거 아닌가?


    






n1 = int(input())
data = []
for _ in range(n1):
    data.append(int(input()))
#print(data)
count = [0 for _ in range(max(data)+1)] 
result = [0 for _ in range(len(data))]  

#예제 data[5 2 3 1 4 2 3 5 1 7]
#그럼 count[0,0,0,0,0,0,0,0]가 생성됨
#결과는 res[0,0,0,0,0,0,0,0,0,0]

Counting(data,count,result)
for a in result:
    print(a)
    
    
일단 이 코드는 메모리 초과가 떠서 틀렸다. 그런데 작성하면서 카운팅정렬을 이해하려고 쓴 주석들이 너무 길어서 써둠

밑은 메모리초과 안넘기기 위해 쓴 코드
https://yoonsang-it.tistory.com/49 님의 코드를 참고했는데 그냥 똑같다..


import sys

n = int(sys.stdin.readline())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(sys.stdin.readline())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)
