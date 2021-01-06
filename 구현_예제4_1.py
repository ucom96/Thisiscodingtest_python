n=int(input())
directions=list(input().split()) # list()를 안해줘도 공백으로 입력받으면 자동으로 리스트 처리됨

coordX=1
coordY=1

for direction in directions:
    if direction=="L":
        coordY-=1
    elif direction=="R":
        coordY+=1
    elif direction=="U":
        coordX-=1
    elif direction=="D":
        coordX+=1

    if coordX==0:
        coordX+=1
    if coordY==0:
        coordY+=1
    if coordX==n+1:
        coordX-=1
    if coordY==n+1:
        coordY-=1

print(coordX,coordY,end="")
