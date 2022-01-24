n = list(input().upper()) #괄호가 하는 역할은 뭘까
l2 = []
for i in set(n):
    l2.append([n.count(i),i])
l1 = sorted(l2,reverse = True)
if len(l1) == 1:
    print(l1[0][1])
elif l1[0][0] == l1[1][0]:
    print('?')
else:
    print(l1[0][1])
    

알파벳 소,대문자 구별은 안한다고 해서 인풋받을때 전부 대문자로 받기로 했다
set(n)으로 중복되는 문자를 전부 없애주고 각 알파벳마다 리스트 안에 있는 수를 count로 세어서 세 리스트에 [알파벳 수,알파벳] 순으로 추가해줬다
그다음 sort해서 수가 가장 큰대로 정렬 한 후 0번째와 1번째의 개수가 동일할 때 ?를 출력하게 만들었다
끗
