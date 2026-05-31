from io import BytesIO
from PIL import Image
import requests

url = "https://picsum.photos/20"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

print(img)
img.show()