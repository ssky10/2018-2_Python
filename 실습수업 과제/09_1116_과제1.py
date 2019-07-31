import random

i = 0
while i < 3:
    a = random.randint(1,100)
    b = random.randint(1,100)    
    while True :
        answer = int(input("%d + %d = " %(a,b)))
        if a+b == answer:
            i += 1
            print("정답입니다!\n")
            break
        
print("총 정답수 : %d 개" %i)
