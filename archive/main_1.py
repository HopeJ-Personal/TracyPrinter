print('Hello world')

# [ Import ]
import turtle

# [ Config ]
srcWidth = 2
srcHeight = 5

# [ Setup ] Window
window = turtle.Screen()

sizes = [srcWidth,srcHeight]
scrnWidth = srcWidth / max(sizes)
scrnHeight = srcHeight / max(sizes)
window.setup(width=scrnWidth,height=scrnHeight)
pxlWidth = window.window_width()
pxlHeight = window.window_height()
window.bgcolor("white") 
window.title("My Drawing Window")

# [ Setup ] Turtle
t = turtle.Turtle()
t.shape("turtle") 
t.color("blue") 

# [ Main Code ]
globalRad = ( pxlWidth / srcWidth ) / 2

## [ Functions ]
def drawPixel(colorParam):
    t.color(colorParam)
    t.circle(globalRad)

t.goto((-pxlWidth/2)+globalRad,globalRad)
for y in range(srcHeight):
    for x in range(srcWidth):
        drawPixel("black")
        t.forward(globalRad*2)
    t.backward(pxlWidth)
    t.right(90)
    t.forward(globalRad*2)
    t.left(90)

# [ Requirement ] Keep the window open until clicked
window.exitonclick()