def Avg(scores):
  total = 0
  for i in scores:
    total += i
  return total/len(scores)

def Max_Min_index(scores):
  max_idx = 0
  min_idx = 0
  for i in range(1,len(scores),1):
    if scores[max_idx] < scores[i]:
      max_idx = i
    if scores[min_idx] > scores[i]:
      min_idx = i
  return max_idx, min_idx

def input_score(name, subject, score_list):
  score = int(input("%s의 %s점수:" %(name,subject)))
  score_list.append(score)
  return score

name = []; kor = []; mat = []; eng = []; sci = []; avg = []

i=1
while True :
  tmp_name = input("%d번 이름:" %i)
  if tmp_name == "마지막":
    break
  name.append(tmp_name)
  tmp_list = []
  tmp_list.append(input_score(tmp_name,"국어",kor))
  tmp_list.append(input_score(tmp_name,"수학",mat))
  tmp_list.append(input_score(tmp_name,"영어",eng))
  tmp_list.append(input_score(tmp_name,"과학",sci))
  avg.append(Avg(tmp_list))
  i += 1

if len(name) != 0 :
  print("이름\t국어\t수학\t영어\t과학\t평균","-"*45,sep="\n")
  
  for i in range(len(name)):
    print("%s\t%d\t%d\t%d\t%d\t%.2f" %(name[i],kor[i],mat[i],eng[i],sci[i],avg[i]))
  
  print("-"*45, "평균\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f" %(Avg(kor), Avg(mat), Avg(eng), Avg(sci), Avg(avg)), "-"*45, sep="\n")

  max_idx,min_idx = Max_Min_index(avg)

  print("최고 평균: %s   %.2f점" %(name[max_idx], avg[max_idx]))
  print("최저 평균: %s   %.2f점" %(name[min_idx], avg[min_idx]))
else:
  print("입력된 데이터가 없습니다.")
