name = []; kor = []; mat = []; eng = []; sci = []

i=1
tmp = input("%d번 이름:" %i)
while tmp != "마지막" :
  name.append(tmp)
  kor.append(int(input("%d번 국어점수:" %i)))
  mat.append(int(input("%d번 수학점수:" %i)))
  eng.append(int(input("%d번 영어점수:" %i)))
  sci.append(int(input("%d번 과학점수:" %i)))
  i += 1
  tmp = input("%d번 이름:" %i)

print("이름\t국어\t수학\t영어\t과학\t평균","-"*45,sep="\n")
min_stu = ["",101]
max_stu = ["",-1]
n=i-1
i=0
kor_sum = 0; mat_sum = 0; eng_sum = 0; sci_sum = 0; avg_sum = 0
while i < n:
  avg = (kor[i]+mat[i]+eng[i]+sci[i])/4
  print("%s\t%d\t%d\t%d\t%d\t%.2f" %(name[i],kor[i],mat[i],eng[i],sci[i],avg))
  kor_sum += kor[i]
  mat_sum += mat[i]
  eng_sum += eng[i]
  sci_sum += sci[i]
  avg_sum += avg
  if min_stu[1] > avg :
    min_stu = [name[i],avg]
  if max_stu[1] < avg :
    max_stu = [name[i],avg]
  i += 1
print("-"*45, "평균\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" %(kor_sum/n, mat_sum/n, eng_sum/n, sci_sum/n, avg_sum/n), "-"*45, sep="\n")

print("최고 평균: %s   %.2f점" %(max_stu[0],max_stu[1]))
print("최저 평균: %s   %.2f점" %(min_stu[0],min_stu[1]))
