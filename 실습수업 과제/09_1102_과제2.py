import turtle

t = turtle.Turtle()
t.shape("turtle")

n = int(turtle.textinput("n각형 그리기","몇각형을 원하시나요?"))
length = int(turtle.textinput("n각형 그리기","한변의 길이는?"))

for i in range(n):
    t.forward(length)
    t.left(360/n)

input()