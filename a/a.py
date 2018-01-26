import numpy as np

# $ pip install pillow
from PIL import Image

img = Image.new('HSV', (640, 480), (255,255,255))
for y in range(480):
    for x in range(640):
        h = (y+1) / (x+1)
        s = np.arctan(h)
        h = int(round((h * 4/3) * 255 % 255))
        s = int(round((s / 2*np.pi) * 255))
        v = 255
        c = (h,s,v)
        img.putpixel((x,y),c)

img = img.convert('RGB')
img.save('a.png', 'PNG')
