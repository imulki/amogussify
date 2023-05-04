from importlib.resources import path
import sys
import imageio.v2 as imageio
from imageio.core.util import Array
from numpy import array as npArray, uint8

# from main import amogussifyPixel 

pattern = [
    [1,1,1,0,0,0,0,0],
    [1,0,1,1,0,0,0,0],
    [1,1,1,1,0,0,0,0],
    [1,0,1,0,0,0,0,0],
    [0,0,0,0,1,1,1,0],
    [0,0,0,0,1,0,1,1],
    [0,0,0,0,1,1,1,1],
    [0,0,0,0,1,0,1,0],
]

# PARAMS
# -s : source image path
# -d : destination image path
def main():
  print("HELLO WORLD")
  MIN_ARGC = 3

  argc = len(sys.argv)

  if (argc < MIN_ARGC):
    print("NOT ENOUGH ARGUMENTS")
    exit()

  srcImagePath = sys.argv[1]
  destImagePath = sys.argv[2]

  image: Array = imageio.imread(srcImagePath)

  print("Total row: ", image.shape[0])
    
  amogussify(image)

  imageio.imwrite(destImagePath, image)

def amogussify(rawImageMatrix: Array):
    # convertedRowList = []
    i = 0

    for row in rawImageMatrix:
        amogussifyRow(row, i)
        i = (i + 1) % len(pattern)

def amogussifyRow(rawRow: Array, rowIdx: int):
    j = 0
    for pixel in rawRow:
        amogussifyPixel(pixel, rowIdx, j)
        j = (j+1) % len(pattern[0])

def amogussifyPixel(rawPixel: Array, rowIdx: int, colIdx: int):
    if (pattern[rowIdx][colIdx] == 1):
        r = rawPixel[0]
        g = rawPixel[1]
        b = rawPixel[2]

        rRev = uint8(255 if r > 170 else r*1.5)
        gRev = uint8(255 if g > 170 else g*1.5)
        bRev = uint8(255 if b > 170 else b*1.5)

        rawPixel[0] = rRev
        rawPixel[1] = gRev
        rawPixel[2] = bRev

main()