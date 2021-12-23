import turtle
import time

screen = turtle.Screen()
screen.register_shape('C:\\Users\\cjdel\Downloads\\circle.gif')
t=turtle.Turtle()
t.shape('C:\\Users\\cjdel\\Downloads\\circle.gif')

screen.setup(1000,1000)
t.speed(0)
t.hideturtle()
x = 0
wheel_numbers = [0, 26, 3, 35, 12, 28, 7, 29, 18, 22, 9, 31, 14, 20,
                 1, 33, 16, 24, 5, 10, 23, 8, 30, 11, 36, 13, 27, 6,
                 34, 17, 25, 2, 21, 4, 19, 15, 32]

t.up()
t.home()
t.setheading(90)
t.left(90)
t.forward(25)
t.right(90)
t.left(360/74)
t.width(5)
t.color('black')

#draw spokes
for x in range(0,37):
    t.color('black')
    t.down()
    t.forward(293)
    t.backward(293)
    t.up()
    t.left(360/37)

t.up()
t.home()
t.setheading(90)
t.forward(300)
t.left(90)

#draw outside
t.down()
t.width(10)
for x in range(0,37):
    if x == 0:
        t.color('green')
    elif x % 2 == 0:
        t.color('red')
    else:
        t.color('black')
    t.forward(50)
    t.left(360/37)

t.up()
t.home()
t.setheading(90)
t.left(90)
t.forward(25)
t.right(90)

#write numbers
for x in range(0,37):
    t.forward(325)
    if x == 0:
        t.color('green')
        t.write(wheel_numbers[x], False, font=("Arial", 14, 'bold'))
    elif x % 2 == 0:
        t.color('red')
        t.write(wheel_numbers[x], False, font=("Arial", 14, 'bold'))
    else:
        t.color('black')
        t.write(wheel_numbers[x], False, font=("Arial", 14, 'bold'))
    t.backward(325)
    t.left(360/37)

import random
wheel_outcome = int(random.choice(wheel_numbers))
player_choice = input("Select a number to bet: ")
player_choice = int(player_choice)
if player_choice == wheel_outcome:
    print("Winner")
else:
    print("Loser")
    print("Winning number: ", wheel_outcome)

t.speed(10)
t.up()
t.home()
t.forward(400)
t.setheading(90)
t.showturtle()
for x in range(0,2):
    t.circle(400)
position_winner = wheel_numbers.index(wheel_outcome)
t.circle(400, (((360/37)*position_winner)+90))
t.left(90)
t.forward(80)
input("Done? ")
