num = int(input("정수를 입력하세요:"))

for i in range(num,0,-1):
    check = 0
    for j in range(i,0,-1) :
        if i%j == 0 :
            check += 1
    if check == 2 :
            print(i)
