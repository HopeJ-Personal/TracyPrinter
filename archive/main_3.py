import turtle
screen = turtle.Screen()
screen.setup(400,400)
screen.title("Turtle Sandbox")
screen.bgcolor("white")

t = turtle.Turtle()
t.speed(0)

srcWidth = 1
srcHeight = 5
sizes = [srcWidth,srcHeight]
scrnWidth = srcWidth / max(sizes)
scrnHeight = srcHeight / max(sizes)
pxlWidth = 400 * scrnWidth
pxlHeight = 400 * scrnHeight

print(pxlWidth,pxlHeight)

globalRadius = 400/max(sizes)
def dot(colorParam):
    t.color(colorParam)
    t.circle(globalRadius)

#t.goto(-globalRadius*srcWidth,((globalRadius*srcHeight)/2)-globalRadius*2)
startX = -200 + globalRadius
startY = 200 - globalRadius

t.penup()
t.goto(startX, startY)
t.pendown()

print(globalRadius*srcHeight)
for y in range(srcHeight):
    for x in range(srcWidth):
        dot("red")
        t.forward(globalRadius*2)
    t.penup()
    t.goto(startX, startY - (globalRadius * 2 * (y + 1)))
    t.pendown()
turtle.done()