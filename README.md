# pixelart-color-regulator
This script was made to replace color pixels in pixelart animation sheets when the colors are slightly off the original (sometimes this happens the copypasting or not using default palette).


Single Image fix:


python3 ColorFixTool.py colorPalette.png imageToFix.png


Batch Image fix:


python3 ColorFixTool.py colorPalette.png batch


EXAMPLE OUTPUT


Width 10, Height: 10

All the different corrections made:

d39787 -> dc9380

dd90a0 -> dc9380

155b3b -> 17502c

Total pixels: 22

Total errors: 3

Percentage of color error: 13.636%


For the batch fix you have to put your files in a folder named 'input' and have an 'output' folder next to it.


The color palette you have to provide can be a normal image or good spritesheet you know that have all the correct colors.


You can check all the colors in the spritesheet with another script that is in this project like this:


python3 getPalette.py image.png
