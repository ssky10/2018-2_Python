kor = int(input("국어 점수를 입력하세요:"))
mat = int(input("수학 점수를 입력하세요:"))
eng = int(input("영어 점수를 입력하세요:"))
sci = int(input("과학 점수를 입력하세요:"))

total = kor+mat+eng+sci
avg = total/4

if  avg >= 90 :
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

print("총점:%d, 평균:%.2f, 학점:%s" %(total,avg,grade))