# 학생수 입력
n=int(input())

infos=[]
# 이름과 점수 리스트 형태로 입력
for _ in range(n):
    infos.append(input().split())

# 리스트를 튜플로 바꿔서 정렬
# 튜플을 원소로 하는 리스트는 기본적으로 튜플의 원소의 순서에 맞게 정렬됨
infos.sort(key=lambda x:(-int(x[1]),int(x[2]),-int(x[3]),x[0]))

# 정렬된 리스트에서 학생 이름을 출력
for student in infos:
    print(student[0])



