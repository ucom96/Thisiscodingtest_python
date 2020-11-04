#문자열 입력
S=input()
#알파벳 리스트
alp=[]
#숫자 리스트
num=[]
#결과리스트
result=[]
#알파벳과 숫자 구별
for i in S:
    if int(ord(i))>=65 and int(ord(i))<=90:
        alp.append(i)
    else:
        num.append(i)

#알파벳 정렬
alp=sorted(alp)
#숫자 합
num=sum(map(int,num)) #sum을 하면 하나의 int형태로 반환 (list형태로 반환안됨)
result.extend(alp) #extend는 리스트에 리스트를 추가하는것
result.append(num)
#결과 출력
print(result)