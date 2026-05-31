# Setup Turtle and Screen
import turtle
screen = turtle.Screen()
screen.setup(400,400)
screen.title("TracyPrinter")
screen.bgcolor("white")

# Configure Turtle
t = turtle.Turtle()
t.speed(0)

# Image Extraction
from io import BytesIO
from PIL import Image
import requests

def extractData(path):
    if path.startswith("http://") or path.startswith("https://"):
        res = requests.get(path)
        img = Image.open(BytesIO(res.content)).convert("RGBA")
    else:
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

#src = "20x20justaguy.png"
src = "https://picsum.photos/10"

# Create variables
width, height, colors = extractData(src)
print(width, height, colors)

dimensions = [width, height]
screenSize = screen.window_width()
globalRadius = (screenSize/2)/max(dimensions)

# Drawing
def drawDot(colorParam):
    t.color(colorParam)
    t.begin_fill()
    t.circle(globalRadius)
    t.end_fill()

sx = -(globalRadius*width)+globalRadius
sy = (globalRadius*height-1)-globalRadius*2
t.goto(sx, sy)

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

# Prevent drawing window from closing upon completion
turtle.done()