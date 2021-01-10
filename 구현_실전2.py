#위치입력받기
location=input()

#이동할 수 있는 경우의 수
count=0
#행과 열을 이동할 경우 연산이 필요하므로 현위치의 행,열을 int형태로 바꿔줄것
col=ord(location[0])
row=int(location[1])

#이동하는 거리의 경우의수 리스트
moves=[[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

#이동하는 거리의 경우의수를 하나씩 살펴봐야하므로 for문으로 돌림
for move in moves:
    #새로운 변수에 현위치에서 이동한 거리를 넣음
    move_row=row+move[1]
    move_col=col+move[0]
    #이동한 위치가 밖으로 벗어나지 않았다면
    if 1<=move_row<=8 and ord('a')<=move_col<=ord('h'):
        #count변수를 증가시킴
        count+=1

print(count)

