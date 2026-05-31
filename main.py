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

from PIL import Image

def extractData(path):
    img = Image.open(path).convert("RGBA")
    
    width, height = img.size
    pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            r, g, b, a = img.getpixel((x,y))
            hex = f"#{r:02x}{g:02x}{b:02x}"
            row.append(hex)
        pixels.append(row)
    return width, height, pixels

#src = "5x5smiley.png"
#src = "15x15faces.png"
#src = "20x20justaguy.png"
src = "jaden-photo1_13percent_25percent.png"
print(extractData(src))
width, height, colors = extractData(src)

#width = 3
#height = 3
dimensions = [width, height]
screenSize = screen.window_width()
globalRadius = (screenSize/2)/max(dimensions)

#colors = [["red","green","blue"],["red","green","blue"],["red","green","blue"]]

def drawDot(colorParam):
    t.color(colorParam)
    t.begin_fill()
    t.circle(globalRadius)
    t.end_fill()

t.goto(-(globalRadius*width)+globalRadius, (globalRadius*height-1)-globalRadius*2)

for y in range(height):
    for x in range(width):
        colorParam = colors[y][x]
        drawDot(colorParam)
        t.forward(globalRadius*2)
    t.backward((globalRadius*2)*width)
    if y != height-1:
        t.right(90)
        t.forward(globalRadius*2)
        t.left(90)

turtle.done()