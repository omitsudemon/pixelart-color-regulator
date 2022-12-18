from PIL import Image
import sys

if len(sys.argv) != 3:
    print("""
    Usage:
    python3 ColorFixTool.py colorPalette.png imageToFix.png
    """)
    exit()

paletteDir = sys.argv[1]
filename = sys.argv[2][:-4]
extension = sys.argv[1][-4::]
picture = Image.open(filename+extension)
palette = Image.open(paletteDir)
print("Width {0}, Height: {1}".format(picture.width, picture.height))
paletteColors = palette.getcolors()

mode = picture.mode

if mode == 'P':
    print('Image is in palette mode. Press y to convert to RGB, or n to exit. (then press enter)')
    option = input()
    if option == 'y':
        picture = picture.convert('RGBA')
    else:
        exit()

def hexToRGB(hexcolor):
    return tuple(int(hexcolor[i:i+2], 16) for i in (0, 2, 4))

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
"""
Returns the similarity between 2 hex colors
"""
def colorSimilarity(color1, color2):
    r1, g1, b1 = hexToRGB(color1)
    r2, g2, b2 = hexToRGB(color2)
    red = abs(r1 - r2)
    green = abs(g1 - g2)
    blue = abs(b1 - b2)
    total = red + green + blue
    total = 765 + total
    total = 765 / total

    return total

#selectedPalette = paletteFemale
selectedPalette = extractPalette(paletteColors)

"""
Returns array with similarity with all the palette's colors and a hex color
Maybe there could be a slight chance of very similar colors in the palette, so I'm storing all possibilities.
"""
def similarityArray(color):
    output = []
    for p in selectedPalette:
        output.append(colorSimilarity(p, color))
    return output

totalPixels = 0
totalErrors = 0
corrections = []



for x in range(picture.width):
    for y in range(picture.height):
        r,g,b,a = picture.getpixel( (x, y) )
        if a != 0: #transparent, also could check if transparency is always 255
            totalPixels += 1
            hexcolor = RGBToHex((r,g,b))
            if hexcolor not in selectedPalette:
                totalErrors += 1
                #print("Red: {0}, Green: {1}, Blue: {2}, Alpha: {3}".format(r,g,b,a))
                #print(hexcolor)
                arr = similarityArray(hexcolor)
                sim = 0
                pos = -1
                for i in range(len(arr)):
                    if arr[i] > sim:
                        sim = arr[i]
                        pos = i
                correction = [hexcolor, selectedPalette[pos]]
                if correction not in corrections:
                    corrections.append(correction)
                selectedColor = hexToRGB(selectedPalette[pos])
                sR, sG, sB = selectedColor
                picture.putpixel((x,y), (sR, sG, sB, 255))
                
picture.save(filename+'-fixed-'+extension)
print('All the different corrections made:')
for cor in corrections:
    print(cor[0] + ' -> ' + cor[1])
print('Total pixels: {0}'.format(totalPixels))
print('Total errors: {0}'.format(totalErrors))
print('Percentage of color error: {0:.3f}%'.format((totalErrors / totalPixels)*100))
#picture.show()
