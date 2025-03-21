import turtle
window = turtle.Screen()
window.setup(600,400)
window.bgcolor("forestgreen")
t=turtle.Turtle()
t.seth(0)
for _ in range(4):
    t.forward(100)
window.mainloop()
