# 문자열 s 입력받기
s=input()

sortedS=[]
summary=0
# for문으로 문자열 s의 문자를 하나씩 받아 알파벳인지 숫자인지 구분
for i in s:
    if ord(i)>=48 and ord(i)<=57:
        summary += int(i)
    else:
        sortedS.append(i)

sortedS.sort()
sortedS.append(summary)

print(sortedS)