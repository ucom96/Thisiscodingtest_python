s=input()

result=int(s[0])

for i in range(len(s)-1):
    if int(s[i])==0 or int(s[i])==1:
        result=result+int(s[i+1])
    else:
        result=result*int(s[i+1])

print(result)