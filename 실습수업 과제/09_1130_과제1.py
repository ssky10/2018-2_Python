score = []
print("5명의 평가 점수를 입력하세요!(100점 만점)")

for i in range(5):
    score.append(int(input("점수 입력 :")))

print("\n==총 입력 점수==")
for i in score:
    print(i,"점")

print("\n==제거 대상 점수==")
max_num = score[0]; min_num = score[0]
for i in score[1:]:
    if max_num < i:
        max_num = i
    if min_num > i:
        min_num = i
print("최고 점수:",max_num,"점")
print("최소 점수:",min_num,"점")
score.remove(max_num)
score.remove(min_num)

print("\n==최종 입력 점수==")
total = 0
for i in score:
    print(i,"점")
    total += i

print("\n"+("="*18))
print("총점:",total,"점")
print("평균:",total/len(score),"점")



