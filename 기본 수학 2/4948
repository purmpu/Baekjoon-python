처음 썼던 코드가
while 1:
  M = int(input())
  if M == 0:
    break
  N = 2*M
  li2 = []
  for i in range(M+1,N+1):
      ic = 0
      if i == 1:
          ic += 1
      for k in range(2,i):
          if i % k == 0:
              ic += 1
              break
      if ic == 0:
          li2 += [i]
  print(len(li2))
  이건데 시간초과가 떠서 구글링을 열심해 해봤다.
  대부분의 사람들이 에라토스테네스의 체를 사용해서 풀었는데 
  https://ooyoung.tistory.com/95 이분은 정말 독창적인 방법으로 푸셔서 이 방법을 써보기로 했다.
  코드를 한번 보고 기억나는대로 쓴 다음 실행, 에러가 뜨면 계속 고치는 방식으로 코드를 작성했다.
  원문을 전부 읽고 이해 한 다음 작성한거라 마지막 while문이 조금 다른것만 제외하면 완전히 일치하지만...
  ...남의 코드를 참고하지 않아도 되는 그날까지 화이팅
  
  pnum = {x for x in range(2,246913) if x == 2 or x % 2 == 1} #2,그리고 246913(입력최대값의 2배+1)전까지의 모든 홀수, 짝수는 구할필요없음
for sqrt in range(3,int((246912**0.5))+1,2): #최대값까지 전부 구해서 지우는게 아닌 최대값의 제곱근까지만 구해서 그 배수를 전부 삭제해도 된다.
  pnum -= {i for i in range(2*sqrt,246913,sqrt) if i in pnum} # 홀수의 배수를 전부 삭제

while 1:
  m = int(input())
  l = []
  if m == 0:
    break
  for y in range(m+1,2*m+1):
    if y in pnum:
      l.append(y)
  print(len(l))

#계산속도가 왜케 빠르지 ㅁㅊ
