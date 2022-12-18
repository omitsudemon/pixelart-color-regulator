from PIL import Image
import sys 
"""
returns a list of (q, (r, g, b, a))
q = quantity
"""
picture = Image.open(sys.argv[1])


def RGBToHex(tuple):
    return '%02x%02x%02x' % (tuple[0], tuple[1], tuple[2])

def extractPalette(palette):
    output = []
    for p in palette:
        q, pal = p
        r, g, b, a = pal
        if a == 255:
            output.append(RGBToHex((r,g,b)))
    return output

print(extractPalette(picture.getcolors()))