# 학생수 n 입력
n=int(input())

array=[]
# 학생의 이름과 성적을 공백으로 구분하여 입력
for i in range(n):
    info=input().split()
    array.append((info[0],int(info[1]))) #튜플 형태로 리스트에 저장

# 성적순대로 정렬
array=sorted(array,key= lambda student:student[1])

# 정렬된 리스트에서 이름만 출력
for student in array:
    print(student[0],end=' ')
