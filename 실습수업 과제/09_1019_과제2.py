x = int(input("x축 좌표를 입력하세요:"))
y = int(input("y축 좌표를 입력하세요:"))

if  (x == 0) and (y == 0):
    print("원점")
elif (y == 0):
    print("X축 위의 점이다.")
elif (x == 0):
    print("Y축 위의 점이다.")
elif (x > 0) and (y > 0):
    print("1사분면")
elif (x < 0) and (y > 0):
    print("2사분면")
elif (x < 0) and (y < 0):
    print("3사분면")
else:
    print("4사분면")