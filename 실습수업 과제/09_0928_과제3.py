import turtle
t = turtle.Turtle()
t.shape("turtle")
x = int(input("이동할 좌표의 x값 입력:"))
y = int(input("이동할 좌표의 y값 입력:"))
t.goto(x,y)
dis = (((0-x)**2)+((0-y)**2))**0.5
t.write("선의 길이 = "+str(dis))