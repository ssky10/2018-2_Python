import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = []

color_list.append(input("색상을 입력하세요:"))
color_list.append(input("색상을 입력하세요:"))
color_list.append(input("색상을 입력하세요:"))

dir = int(input("원의 반지름을 입력하세요:"))

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(dir)
t.end_fill()

t.up()
t.fd(dir*2)
t.down()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(dir)
t.end_fill()

t.up()
t.fd(dir*2)
t.down()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(dir)
t.end_fill()

input()