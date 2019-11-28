import turtle, os
import random
import time
import vlc

#draw canvas
wn = turtle.Screen()
wn.setup(width=1000, height=600)
wn.addshape("choc.gif")
wn.addshape("lolipop.gif")
wn.addshape("waffle.gif")
wn.title ("Slot machine by Prosjektplast")
wn.colormode(255)
wn.bgpic("prosjekt.gif")


#make machine border
turtle.penup()
turtle.hideturtle()
turtle.speed(0)
turtle.goto(-300,150)
turtle.color("yellow")
turtle.pendown()
turtle.pensize(8)
for side in range(2):
    turtle.fd(600)
    turtle.right(90)
    turtle.fd(300)
    turtle.right(90)

#make first column
turtle.penup()
turtle.fd(200)
turtle.setheading(270)
turtle.pendown()
turtle.fd(300)

#make second column
turtle.penup()
turtle.setheading(90)
turtle.fd(300)
turtle.setheading(0)

#make third column
turtle.fd(200)
turtle.setheading(270)
turtle.pendown()
turtle.fd(300)

#Makes 3 graphics for slot machine
    #Make the first box
shape1 = turtle.Turtle() #This is a stationary turtle
shape1.speed(0)
shape1.penup()
shape1.goto(-200,0)
shape1.setheading(90)
shape1.shapesize(5)
shape1.shape("choc.gif")


    #Make the second box
shape2 = turtle.Turtle()
shape2.speed(0)
shape2.penup()
shape2.shape("lolipop.gif")
shape2.setheading(90)
shape2.shapesize(5)

    #Make the third box
shape3 = turtle.Turtle()
shape3.speed(0)
shape3.penup()
shape3.goto(200,0)
shape3.shape("waffle.gif")
shape3.setheading(90)
shape3.shapesize(5)

#Create announce turtle
done = turtle.Turtle()
done.speed(0)
done.penup()
done.hideturtle()
done.goto(0,200)

#Opening credits
done.write ("Congratulations you answered more than 5 correct answers!", align="center", font=("fixedsys",30,"bold"))
time.sleep(2)
done.clear()

done.write ("Press s to spin", align="center", font=("fixedsys",30,"bold"))
time.sleep(1.3)
done.clear()


#key functions
def spin0():
    if True:
        global x
        global y
        global z
    #Randomize numbers
    x = random.randint(1,3)
    y = random.randint(1,3)
    z = random.randint(1,3)
#intro()
def spin():
    #shape 1 change
    if x == 1:
        shape1.shape("choc.gif")
    elif x == 2:
        shape1.shape("lolipop.gif")
    elif x == 3:
        shape1.shape("waffle.gif")

    #shape 2 change
    if y == 1:
        shape2.shape("choc.gif")
    elif y == 2:
        shape2.shape("lolipop.gif")
    elif y == 3:
        shape2.shape("waffle.gif")

    #shape 3 change
    if z == 1:
        shape3.shape("choc.gif")
    elif z == 2:
        shape3.shape("lolipop.gif")
    elif z == 3:
        shape3.shape("waffle.gif")


def spin2():
    for action in range (10):
        spin0()
        spin()
        time.sleep(0.3)
    spin3()

def spin3():
    if x == y and x == z:
        done.write ("You won!!!", align="center", font=("Verdana",40,"bold"))
        time.sleep(3)
        done.clear()
    else:
        done.write ("Sorry no luck this time",align="center", font=("Verdana",40,"bold"))
        time.sleep(3)
        done.clear()

wn.listen()
wn.onkeypress(spin2, "s")
turtle.mainloop()
