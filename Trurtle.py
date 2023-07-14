from turtle import *
import turtle
import time
from random import choice

# SCREEN SETUP
setup(800, 800)
title('Turtle Race')
bgcolor('#006666')
speed(0)
tim = turtle.Turtle()
tim.speed(0)

# HEADING
penup()
goto(-100, 250)
color("white")
write('LAZY TURTLE RACE', font=('Helvetica', 20, 'bold'))

# Small square boxes
small_box_size = 10
small_box_spacing = 20
small_box_x = -100
small_box_y = 240

for _ in range(14):
    goto(small_box_x, small_box_y)
    pendown()
    color("light blue")
    begin_fill()
    for _ in range(4):
        forward(small_box_size)
        right(90)
    end_fill()
    penup()
    small_box_x += small_box_spacing


# DIRT
goto(-350, 200)
pendown()
color('#778899')
begin_fill()
for i in range(2):
    forward(700)
    right(90)
    forward(400)
    right(90)
end_fill()

# FINISH LINE
sq_size = 20
shape("square")
penup()

# WHITE SQUARES ROW 1
color("white")
for i in range(10):
    goto(250, (170 - (i * sq_size * 2)))
    stamp()

# WHITE SQUARES ROW 2
for i in range(10):  # Change from 10 to 9
    goto(250 + sq_size, ((210 - sq_size) - (i * sq_size * 2)))
    stamp()

# BLACK SQUARES ROW 1
color("black")
for i in range(10):
    goto(250, (190 - (i * sq_size * 2)))
    stamp()

# BLACK SQUARES ROW 2
for i in range(10):  # Change from 10 to 9
    goto(251 + sq_size, ((190 - sq_size) - (i * sq_size * 2)))
    stamp()

# Border line
border_size = 20
shape("square")
penup()

# WHITE Top
color("white")
for i in range(18):
    goto(-340 + (i * border_size * 2), 205)
    stamp()

# Bottom
for i in range(18):
    goto(-340 + (i * border_size * 2), -205)
    stamp()

# Red
color("red")
for i in range(17):
    goto(-320 + (i * border_size * 2), 205)
    stamp()

# Bottom Red
for i in range(17):
    goto(-320 + (i * border_size * 2), -205)
    stamp()

# Define turtles attributes
turtle_data = [("blue", 150), ("white", 50), ("purple", -50), ("yellow", -150)]

# Create and setup turtles
turtles = []
for color, position in turtle_data:
    turtle = Turtle()
    turtle.color(color)
    turtle.shape('turtle')
    turtle.shapesize(1.5)
    turtle.penup()
    turtle.goto(-300, position)
    turtle.pendown()
    turtles.append(turtle)


# COUNTDOWN
text_turtle = Turtle()
text_turtle.hideturtle()

# Countdown timer
for i in range(3, 0, -1):
    text_turtle.clear()
    text_turtle.penup()
    text_turtle.goto(0, 0)
    text_turtle.color('white')
    text_turtle.write(str(i), align='center', font=('Helvetica', 55, 'bold'))
    time.sleep(1)
text_turtle.clear()


# Move the turtles
while all(turtle.xcor() <= 230 for turtle in turtles):
    for turtle in turtles:
        turtle.forward(choice(range(1, 11)))

# Winner
winner = max(turtles, key=lambda turtle: turtle.xcor())
winner_color = winner.color()[0].capitalize()  # Get the color of the winner

# Celebrate the winner
for _ in range(72):
    winner.right(5)
    winner.shapesize(3)

winner_message = f'{winner_color} Turtle WINS!'

# Display winner
text_turtle.color('white')
text_turtle.write(winner_message, font={'family':'oswald', 'size': 200, 'weight': 'bold'})
time.sleep(1)
text_turtle.clear()

# Firework celebration
def pen(colour):
    tim.color(colour)

def firework1(size):
    for num in range(20):
        tim.fd(size)
        tim.rt(180-(360/20))

def move():
    tim.pu()
    x = choice(range(-150, 151))
    y = choice(range(-150, 151))
    tim.goto(x, y)
    tim.pd()

# Start firework celebration
move()
pen('red')
firework1(60)
move()
pen('yellow')
firework1(30)
move()
pen('blue')
firework1(57)
move()
pen('purple')
firework1(80)
move()
pen('lightblue')
firework1(120)
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(54)
move()
pen('violet')
firework1(33)
move()
pen('green')
firework1(68)
move()
pen('gold')
firework1(150)
move()
pen('silver')
firework1(47)
move()
pen('darkgreen')
firework1(99)

# Additional fireworks
for _ in range(10):
    move()
    pen(choice(['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']))
    firework1(choice(range(30, 151)))

# Done
done()
