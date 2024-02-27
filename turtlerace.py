import turtle
import time
import random

WIDTH, HEIGHT=500,500
COLORS=['red','green','blue','brown','cyan','black','yellow','purple','grey','pink']
def init_turtle():
    screen=turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title("Turtle racing")

def get_turtles():
    while True:
        turtles=input("enter the number of turtles you want to race: ")
        if turtles.isdigit():
            turtles=int(turtles)
        else:
            print("try agian")
            continue
        if 2<=turtles<=10:
            return turtles
        else:
            print("number should be in range(2-10)")

def race(colors):
    turtles=create_turtle(colors)
    while True:
        for racer in turtles:
            distance=random.randrange(1,20)
            racer.forward(distance)

            x,y=racer.pos()
            if y>=HEIGHT//2-10:
                return colors[turtles.index(racer)]

def create_turtle(colors):
    turtles=[]
    space=WIDTH//(len(colors)+1)
    for i,color in enumerate(colors):
        racer=turtle.Turtle()
        racer.shape('turtle')
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1)*space,-HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

racers=get_turtles()
init_turtle()
random.shuffle(COLORS)
colors=COLORS[:racers]
winner=race(colors)
print("The winner is ",winner)
time.sleep(5)

# racer=turtle.Turtle()
# racer.speed(2)
# racer.shape('turtle')
# racer.color('cyan')
# racer.forward(100)
# racer.left(90)
# racer.forward(100)
# racer.left(90)
# racer.backward(100)
# time.sleep(5)