# This file was created by Joshua Petrus
# Source: https://gist.github.com/wynand1004/ec105fd2f457b10d971c09586ec44900
# By @TokyoEdTech
# I commmented it out trying to understand it
import turtle
import time
import random
# delay until next round
delay = 0.1

# Score continuing throughr ounds
score = 0
high_score = 0

# Start up
wn = turtle.Screen()
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) 
# Turns off the screen

# Snake head features
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake food to make snake bigger
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Times New Roman", 24, "normal"))

# Functions to move snake
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":  
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Moving keys
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Working while true
while True:
    wn.update()

    # Collisions
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        # Hiding segments
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Clear the list
        segments.clear()

        # Score shown(reset)
        score = 0

        # Delay(reset)
        delay = 0.1

        # Font and words on game
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Rman", 24, "normal")) 


    # Bumbing into food
    if head.distance(food) < 20:
        # Food being moved to random spots in the game
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        # New segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.penup()
        segments.append(new_segment)
        
        # Delay
        delay -= 0.001

        # Score increased for eating food
        score += 10

        if score > high_score:
            high_score = score
        # Pen used for font and words on game
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Roman", 24, "normal")) 

    # Range and segments 
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

    # Head bumbing into body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            # Hiding the segments
            for segment in segments:
                segment.goto(1000, 1000)
        
            # Clear
            segments.clear()

            # Score shown(reset)
            score = 0

            # Delay(reset)
            delay = 0.1
        
            # Score shown with text 
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Times New Roman", 24, "normal"))
    #Delay
    time.sleep(delay)

wn.mainloop()