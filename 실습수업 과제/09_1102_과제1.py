num = int(input("정수를 입력하세요 : "))

fac = 1

for i in range(2,num+1,1):
    fac *= i

print("%d!의 값은 %d입니다." %(num,fac))