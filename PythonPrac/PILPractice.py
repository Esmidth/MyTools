__author__ = 'Esmidth'

from PIL import Image
from PIL import PSDraw

im = Image.open("/Users/Esmidth/Pictures/FontTest.png")
number = Image.open("/Users/Esmidth/Desktop/No.5.tiff")

layer = Image.new("RGBA", number.size, (0, 0, 0, 0))

layer.paste(number)

img1 = Image.composite(layer, im, layer)
img1.show()
