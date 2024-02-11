from turtle import *

#we want to paint a house

#we want to paint a house

width(7)
color("purple")
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
color("yellow")
begin_fill()
left(90)
forward(120)  #height of the door
right ( 90)
forward(60)
right(90)
forward(120)  
end_fill()
penup()
goto(200, 200)
pendown()





color("red")     
begin_fill()
right(150)
forward(200)
left(120)
forward(200)  
end_fill()

#drawing a window

penup()
begin_fill()
color("black")
goto(30,150)
pendown()
left(30)
forward(35)
left(90)
forward(35)
left(90)

forward(35)
left(90)
forward(35)

#last window :))
color ("black")
penup()
goto(170,150)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

exitonclick()