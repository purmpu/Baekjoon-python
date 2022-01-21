문자열 문제를 이제 첨 풀어봤는데 파이썬엔 신기한 함수들이 진짜 많은것 같다
파이썬아 고마워~~!!!


n = input()

al = 'abcdefghijklmnopqrstuvwxyz'

for i in al:
    if i in n:
        print(n.index(i),end = ' ')
    else:
        print(-1,end = ' ')

알파벳을 써주고 포문으로 하나씩 불러내 인풋에 그 알파벳이 있는지 찾아봤다
처음에 변수를 al이 아니라 alpha로 했을때 i가 abcdefg... 통째로 불러와졌었는데 왜인지는 몰르겟음
알수없는 제2외국어의 세계
