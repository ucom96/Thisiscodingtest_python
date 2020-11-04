#점수 입력
score=list(map(int,input()))
#점수 앞부분
front=score[:len(score)//2]
#점수 뒷부분
back=score[len(score)//2:]
#점수 앞/뒷부분 합 구하기
f_sum=sum(front)
b_sum=sum(back)
#점수 앞부분과 뒷부분의 합 비교
if f_sum == b_sum:
    print("LUCKY")
else:
    print("READY")




