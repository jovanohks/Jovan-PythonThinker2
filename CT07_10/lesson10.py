## Task 1: Function without parameter (w/o turtle)
# You are required to print the same "Motion Detected" phrase
# multiple times as part of a motion detecting program that you
# are creating.

# Create an 'alert()' function that will print "Motion Detected"
# whenever the function is called.

# **Example**
# Input:
#     alert()
# Output:
#     Motion Detected
def alert():
    print("MOTION DETECTED!")
# alert()
## Task 2: Function without parameter (w turtle)
# Using the 'turtle' library, create a 'square()' function that
# draws a 20x20 square at the turtle object's current position
# whenever the function is called.

# By calling the 'square()' function, draw a square anywhere
# within the turtle window.
import turtle
import random
window = turtle.Screen()
window.setup(600,400)
t=turtle.Turtle()
t.seth(90)

def square():
    t.pendown()
    for i in range(4):
        t.forward(20)
        t.right(90)
square()
window.mainloop()