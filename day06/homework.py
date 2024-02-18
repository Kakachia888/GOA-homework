from turtle import *

#we want to paint a house

#we want to paint a house
speed(200)

width(7)
goto(-500,0)
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
goto(-430,0)
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
goto(-300, 200)
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
goto(-470,150)
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
goto(-330,150)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)


from turtle import *

#we want to paint a house

#we want to paint a house
penup()
goto(-200,0)
pendown()
width(7)
 
right(90)

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
goto(-0, 200)
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
goto(-170,150)
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
goto(-30,150)
pendown()
forward(35)
left(90)
forward(35)
left(90)
forward(35)
left(90)
forward(35)

penup()
goto(170,150)
pendown()

# Set the fill color to orange and the pen color to yellow
color('orange', 'yellow')

# Begin filling the shape with the current fill color
begin_fill()

# Loop indefinitely (until the program is stopped manually)
while True:
  # Move the turtle forward 350 pixels
  forward(350)
  # Turn the turtle left by 170 degrees
  left(170)
  # Turn the turtle right by 280 degrees
  right(280)

  # Check if the turtle's position is close to the starting point (within 1 pixel)
  if abs(pos()) < 1:
    # If it is, exit the loop
    break

# End the fill operation
end_fill()

# Stop the turtle graphics window from closing immediately
done()


exitonclick()