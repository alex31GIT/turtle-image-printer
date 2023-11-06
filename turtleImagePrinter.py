from PIL import Image
import numpy as np
from turtle import Turtle


def create_draw_plan(array_):
    schema_ = []
    for y_ in range(len(array_)):
        for x_ in range(len(array_[0])):
            print(array_[y_][x_])
            if y_ == 0 and x_ == 0:
                if array_[y_][x_] < 130:
                    schema_.append(-1)
                else:
                    schema_.append(1)
            else:
                if array_[y_][x_] < 130:
                    if schema_[-1] < 0:
                        schema_[-1] -= 1
                    else:
                        schema_.append(-1)
                else:
                    if schema_[-1] > 0:
                        schema_[-1] += 1
                    else:
                        schema_.append(1)

        schema_.append(0)

    return schema_


img = Image.open("StarWars.jpg")
img = img.convert("L")
img_a = np.array(img)

t = Turtle()
t.speed(10000)

x_s = -500
y_s = 300
t.penup()
t.setx(x_s)
t.sety(y_s)
t.pendown()

schema = create_draw_plan(img_a)

for element in schema:
    if element < 0:
        t.pendown()
        t.forward(abs(element))
    elif element > 0:
        t.penup()
        t.forward(element)
    else:
        t.penup()
        t.setx(x_s)
        t.right(90)
        t.forward(1)
        t.left(90)

t.screen.mainloop()


