from turtle import Turtle, Screen
import time
import random

s = Screen()
s.screensize(600,600)
s.bgcolor("black")

scoreSc = Turtle()
scoreSc.penup()
scoreSc.hideturtle()
scoreSc.color("white")
scoreSc.goto(0,290)

t = Turtle()
t.color("white")
t.hideturtle()
t.write("Welcome to Snake Game\nPress space bar to play!",False,"center",("Calibri",20,"normal"))
s.tracer(0)

snake = []

food = Turtle()
food.penup()
food.shapesize(0.8,0.8)
food.shape("square")
food.color("red")

def move():

    prevPos = snake[0].pos()
    snake[0].fd(20)
    snake[0].speed(0)
    headPosX = int(snake[0].xcor())
    headPosY = int(snake[0].ycor())
    headPosX = fixPos(headPosX)
    headPosY = fixPos(headPosY)
    snake[0].goto(headPosX,headPosY)
    
    if headPosX > 300:
        snake[0].setx(-300)
    elif headPosX < -300:
        snake[0].setx(300)
    elif headPosY > 280:
        snake[0].sety(-300)
    elif headPosY < -300:
        snake[0].sety(280)
    for i in range(len(snake)):
        if i>0:
            currentPos = snake[i].pos()
            snake[i].goto(prevPos)
            prevPos = currentPos

    for i in range(len(snake)):
        
        if 0 < i < len(snake)-1:
            frontX = snake[i-1].xcor()
            frontY = snake[i-1].ycor()
            curX = snake[i].xcor()
            curY = snake[i].ycor()
            backX = snake[i+1].xcor()
            backY = snake[i+1].ycor()

            if frontX!=backX and frontY!=backY:
                snake[i].shapetransform(0.8,0,0,0.8)
                if curX == 300 and frontX == -300:
                    None 
                elif curX == -300 and frontX == 300:
                    None
                elif curY == -300 and frontY == 280:
                    None
                elif curY == -300 and frontY == 280:
                    None
                else:
                    snake[i].pendown()


            elif frontX == curX == backX:
                snake[i].shapetransform(1.4,0,0,0.8)
                snake[i].clear()
                snake[i].penup()

            elif frontY == curY == backY:
                snake[i].shapetransform(0.8,0,0,1.4)
                snake[i].clear()
                snake[i].penup()

        elif i == len(snake)-1:

            frontX = snake[i-1].xcor()
            frontY = snake[i-1].ycor()
            curX = snake[i].xcor()
            curY = snake[i].ycor()
            
            if frontX == curX:
                snake[i].shapetransform(1.4,0,0,0.8)

            elif frontY == curY:
                snake[i].shapetransform(0.8,0,0,1.4)

            
def isHitFood():

    for item in snake:
        snakePosX = int(item.xcor())
        snakePosY = int(item.ycor())

        foodPosX = int(food.xcor())
        foodPosY = int(food.ycor())
        if snakePosX == foodPosX and snakePosY == foodPosY:
            return snakePosX == foodPosX and snakePosY == foodPosY

def setFoodPos():
    x = 20*random.randint(-15,15)
    y = 20*random.randint(-15,14)
    food.goto(x,y)

def waitUp():
    if snake[0].ycor() == snake[1].ycor():
        snake[0].setheading(90)        

def waitDown():
    if snake[0].ycor() == snake[1].ycor():
        snake[0].setheading(270)
        
def waitLeft():
    if snake[0].xcor() == int(snake[1].xcor()):
        snake[0].setheading(180)
        
def waitRight():
    if snake[0].xcor() == snake[1].xcor():
        snake[0].setheading(0)
        
    
def turn():
    s.onkey(waitUp,"Up")
    s.onkey(waitDown,"Down")
    s.onkey(waitLeft,"Left")
    s.onkey(waitRight,"Right")

def addTail():
    newTail = Turtle()
    newTail.shape("square")
    newTail.color("white")
    newTail.shapesize(0.8,0.8)
    newTail.penup()
    newTail.pensize(17)
    prevTail = snake[len(snake)-1]
    prevTailX = prevTail.xcor()
    prevTailY = prevTail.ycor()
    newTail.goto(prevTailX,prevTailY)
    snake.append(newTail)

def fixPos(x):
    if x%20 == 19:
        x= x+1
    elif x%20 == 1:
        x = x-1
    return x

def isHitTail():
    headSnake = snake[0]
    headX = headSnake.xcor()
    headY = headSnake.ycor()
    for item in snake:
        if item != headSnake:
            bodyX = item.xcor()
            bodyY = item.ycor()
            if headX == bodyX and headY == bodyY:
                return True


def start():

    if not snake:
        play()


def clearSnake():
    food.hideturtle()
    s.update()
    for item in snake:
        item.clear()
        item.hideturtle()
    snake.clear()

def play():
    food.showturtle()
    score = 0
    scoreSc.clear()
    scoreSc.write(f"Score : {score}",False,"center",("Calibri",20,"normal"))

    t.clear()
    positions = [(0,0),(-20,0),(-40,0)]

    x = 20*random.randint(-15,15)
    y = 20*random.randint(-15,14)
    food.setpos(x,y)

    for pos in positions:
        segment = Turtle()
        segment.penup()
        segment.color("white")
        segment.pensize(17)
        segment.shape("square")
        segment.shapesize(0.8,1.4)
        segment.goto(pos)
        snake.append(segment)


    while True:
        turn()
        s.update
        time.sleep(0.05)
        move()
        s.update()
        time.sleep(0.05)
        turn()
        s.update
        time.sleep(0.05)
        if isHitFood():
            score = score+1
            scoreSc.clear()
            scoreSc.write(f"Score : {score}",False,"center",("Calibri",20,"normal"))
            addTail()
            setFoodPos()
        if isHitTail():
            t.write("Game Over! \n Press space bar to play again!",False,"center",("Calibri",20,"normal"))            
            break
    clearSnake()


s.onkeypress(start,"space")

s.listen()

s.exitonclick()