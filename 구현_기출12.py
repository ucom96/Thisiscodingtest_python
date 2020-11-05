def solution(n, build_frame):
    index=0
    answer = [[]]
    for info in build_frame:
        x,y,stuff,operate=info
        #기둥의 규칙
        if x == 0 or [x - 1, y + 1, 1] in info or [x, y + 1, 0] in info:
            if operate == 1: #기둥을 설치하고자 한다면
                answer.append([x,y,stuff])
            else: # 기둥을 삭제하고자 한다면
                continue
        #보의 규칙
        elif [x, y-1, 0] in info or [x+1, y-1,0] in info or [x-1,y,1] in info and [x+1,y,1] in info:
            if operate == 1: #보를 설치하고자 한다면
                answer.append([x,y,stuff])
            else: #보를 삭제하고자 한다면
                continue

    sorted(answer)
    return answer

n=int(input())
print(solution())