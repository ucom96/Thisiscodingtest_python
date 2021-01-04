s=input()

count0=0
count1=0

#첫번째 원소 확인
if s[0]=='0':
    count0+=1
else:
    count1+=1

#두번째 원소부터 순차적으로 원소끼리의 비교
for i in range(1,len(s)-1):
    if s[i]!=s[i+1]:
        if s[i+1]=='0':
            count0+=1
        else:
            count1+=1

print(count0)
print(count1)
print(min(count0,count1))


