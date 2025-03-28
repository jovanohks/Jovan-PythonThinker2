import turtle
import random
window = turtle.Screen()
window.setup(600,400)
window.bgcolor("forestgreen")
# t=turtle.Turtle()
# t.seth(0)
# t.pendown
# for _ in range(4):
#     t.forward(100)
#     t.left(90)
# t.penup()

# **Task 1b**: Drawing the finish line
# Adding on to your previous answer, create a line of black
# squares at y = 250 by creating a black square turtle object
# and stamping it from x = -300 to x = 300 at 25 pixel-
# intervals

# 1. Create a turtle object named 'pen'
# 2. Lift the pen up
# 3. Using '.shape()', set the turtle object's shape to "square"
# 4. Using '.sety()', set turtle object's y position to 250
# 5. Using a 'for i in range()' loop, use the 'i' variable to
#    create a stamp of 'pen' turtle object from x = -300 to
#    x = 300 at 25-pixel intervals:
#         a. Set 'pen' turtle's x coordinate using '.setx()'
#         b. Stamp a copy of 'pen' turtle at its current
#            position using '.stamp()'

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)
t = turtle.Turtle()
t.shape("square")
t.penup()
t.sety(250)
for i in range(-300,300,25):
    t.penup()
    t.setx(i)
    t.pendown()
    t.stamp()

# **Task 1c**: Drawing the start line
# Adding on to your previous answer, use the 'pen' turtle object
# you have created earlier to draw a horizontal yellow start
# line at y = -250.

# 1. Using '.goto()', set 'pen' turtle's coordinates to
#    (-300, -250)
# 2. Using the following commands, set the colour of 'pen' to
#    "yellow", set heading to 0 and move forward by 600
#    before hiding the turtle:
#         a. '.pencolor()'
#         b. '.pendown()'
#         c. '.seth()'
#         d. '.forward()'
#         e. '.hideturtle()'

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)


t.penup()
t.goto(-300,-250)
t.pencolor("yellow")
t.seth(0)
t.pendown()
t.forward(600)
t.hideturtle()

# **Task 1d**: Create Sally the turtle
# Adding on to your previous answer, create a red, turtle-shaped
# turtle object 'Sally' will be one of the turtle racers.
# Position Sally at the starting position of (0, -250) and put
# "Sally" above the 'Sally' turtle object.

# 1. Using 'turtle.Turtle()', create a 'Sally' turtle object
# 2. Lift the pen using '.penup()'
# 3. Using '.seth()', set 'Sally' turtle's heading to 90
# 4. Using '.shape()', set 'Sally' turtle's shape to "turtle"
# 5. Using '.color()', set 'Sally' turtle to "red"
# 6. Using '.goto()', move 'Sally' turtle to (0, -250)
# 7. Using '.write("Sally", align="center", font=('Arial', 20))',
#    put "Sally" above Sally the turtle

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)
s = turtle.Turtle()
s.penup()
s.seth(90)
s.shape("turtle")
s.color('red')
s.goto(0,-250)
s.pendown()
s.write("Sally", align="center", font=('Arial', 20))


# **Task 1e**: Configure Bob and Keith turtles
# Adding on to your previous answer, repeat what you have done
# to set up Sally the turtle to also create the following
# turtles and position them at the specified coordinates:
# 1. Bob:
#     Colour: "blue"
#     Starting position: (-200, -250)
# 2. Keith:
#     Colour: "white"
#     Starting position: (200, -250)

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)
b = turtle.Turtle()
b.penup()
b.seth(90)
b.shape("turtle")
b.color('blue')
b.goto(-200,-250)
b.pendown()
b.write("bob", align="center", font=('Arial', 20))
k = turtle.Turtle()
k.penup()
k.seth(90)
k.shape("turtle")
k.color('white')
k.goto(200,-250)
k.pendown()
k.write("keith", align="center", font=('Arial', 20))

# **Task 1f**: Input to guess the race winner
# Adding on to your previous answer, ask the user to guess the
# winner and store the user's response in the 'guess' variable

# 1. Using 'input()', ask the user to "Guess the winner! " in
#    the console.
# 2. Store the user's response in the variable 'guess'
guess = input("whats the winner? ")

# **Task 1g**: Racing loop
# Adding on to your previous answer, import the 'random' library
# and create a forever loop that will set each racing turtle's
# heading and number of steps forward randomly until one of them
# crosses y=250 where the finish line is.

# 1. Initiate a variable 'winner' and assign it an empty string
# 2. Set Bob, Sally, and Keith's pen down.
# 3. In a forever loop:
#     a. Use '.seth()' and '.randint()' to set each racing
#        turtle's heading to between 75 and 115 randomly
#     b. Use '.forward()' and 'randint()' to move each racing
#        turtle forward by between 1 and 20 randomly
#     c. Using '.ycor()', create an 'if..elif..elif' statement
#        that checks if any of the racing turtle's y coordinate
#        is higher than y = 250.
#             i. If true, set the 'winner' variable to the
#                winning turtle's name and 'break' out of the
#                forever loop.



while True:
    s.seth(random.randint(75,115))
    b.seth(random.randint(75,115))
    k.seth(random.randint(75,115))
    s.forward(random.randint(1,20))
    s.forward(random.randint(1,20))







































window.mainloop()
