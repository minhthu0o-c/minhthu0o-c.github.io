from turtle import *

title("Simple Car")
pensize(3)
speed(1)
shape("turtle")

# Body
color("blue")
fillcolor("blue")
begin_fill()
forward(200)
left(90)
forward(50)
left(90)
forward(200)
left(90)
forward(50)
end_fill()

# Roof
penup()
goto(50, 50)
pendown()

color("skyblue")
fillcolor("skyblue")
begin_fill()
setheading(0)
forward(100)
left(90)
forward(40)
left(90)
forward(100)
left(90)
forward(40)
end_fill()

# Back Wheel
penup()
goto(50, -20)
pendown()

color("black")
fillcolor("black")
begin_fill()
circle(20)
end_fill()

# Front Wheel
penup()
goto(150, -20)
pendown()

begin_fill()
circle(20)
end_fill()

hideturtle()
done()