import random

# x = random.randint(1,10)

user = input("복권번호를 입력하세요 : ")
num = str(random.randint(10,99))

print("당첨번호는",num,"입니다.")

if ((user[0] == num[0]) and (user[1] == num[1])) or ((user[0] == num[1]) and (user[1] == num[0])):
    print("상금은 100만원 입니다.")
elif ((user[0] == num[0]) or (user[1] == num[1])) or ((user[0] == num[1]) or (user[1] == num[0])):
    print("상금은 50만원 입니다.")
else:
    print("꽝")
