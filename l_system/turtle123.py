from turtle import Turtle

t = Turtle()
t.color("deeppink", "yellow")
t.goto(-150, 0)
t.speed(15)
res_angle = 0
dencity = 40
for i in range(dencity):
    t.forward(300)
    t.left(170)
    res_angle = (res_angle + 170) % 360


def rectangle(w, h, reverse=False):
    sign = -1 if reverse else 1
    for _ in range(2):
        t.forward(w)
        t.left(90*sign)
        t.forward(h)
        t.left(90*sign)
        t.forward(w)
        t.right(90*sign)
        t.forward(h)
        t.right(90*sign)


t.goto(0, 0)

t.right(res_angle)
t.right(180)
t.backward(5)
res_angle = 0

height_flover = 15
t.color("darkorange4", "yellow")
cell_w, cell_h = 10, 5

for i in range(height_flover):
    rectangle(cell_w, cell_h)
    res_angle = (res_angle + 90) % 180


for i in range(height_flover):
    rectangle(cell_w, cell_h, reverse=True)

# t.screen.exitonclick()
t.screen.mainloop()
