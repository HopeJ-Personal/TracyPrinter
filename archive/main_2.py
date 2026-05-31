import turtle
screen = turtle.Screen()
screen.setup(400,400)
screen.title("Turtle Sandbox")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

srcWidth = 10
srcHeight = 40
sizes = [srcWidth,srcHeight]
scrnWidth = srcWidth / max(sizes)
scrnHeight = srcHeight / max(sizes)
pxlWidth = 400 * scrnWidth
pxlHeight = 400 * scrnHeight
print(pxlWidth,pxlHeight)
t.forward(200)

turtle.done()