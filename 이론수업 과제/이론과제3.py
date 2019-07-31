stu_num = int(input("몇 명?:"))
name = []; kor = []; mat = []; eng = []; sci = []

for i in range(stu_num):
  name.append(input("%d번 이름:" %(i+1)))
  kor.append(int(input("%d번 국어점수:" %(i+1))))
  mat.append(int(input("%d번 수학점수:" %(i+1))))
  eng.append(int(input("%d번 영어점수:" %(i+1))))
  sci.append(int(input("%d번 과학점수:" %(i+1))))

print("이름\t국어\t수학\t영어\t과학\t평균")
print("-"*50)
avg = (kor[0]+mat[0]+eng[0]+sci[0])/4
print("%s\t%d\t%d\t%d\t%d\t%f" %(name[0],kor[0],mat[0],eng[0],sci[0],avg))
min_stu = [name[0],avg]
max_stu = [name[0],avg]

for i in range(1,stu_num,1):
  avg = (kor[i]+mat[i]+eng[i]+sci[i])/4
  print("%s\t%d\t%d\t%d\t%d\t%f" %(name[i],kor[i],mat[i],eng[i],sci[i],avg))
  if min_stu[1] > avg :
    min_stu = [name[i],avg]
  if max_stu[1] < avg :
    max_stu = [name[i],avg]

print("최고 평균: %s   %f점" %(max_stu[0],max_stu[1]))
print("최저 평균: %s   %f점" %(min_stu[0],min_stu[1]))
