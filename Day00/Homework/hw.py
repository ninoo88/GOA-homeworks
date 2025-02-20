from turtle import *

#we want to paint a house

#step 1:  draw a square
speed(30)
width(7)

color("light blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square 

#drawing a door

forward(70)
color("light pink")
begin_fill()
left(90)
forward(100) #height of the door
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows

penup()
goto(70, 120)
pendown()

color("purple")
right(60)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(130, 120)
pendown()

left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)

penup()
goto(155, 120)
pendown()

right(180)
forward(50)

penup()
goto(130, 145)
pendown()

right(90)
forward(50)

penup()
goto(45,120)
pendown()

left(90)
forward(50)

penup()
goto(20, 145)
pendown()

right(90)
forward(50)

penup()
goto(120, 50)
pendown()

forward(5)





exitonclick()