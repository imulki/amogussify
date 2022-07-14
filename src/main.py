import sys
import imageio.v2 as imageio
from imageio.core.util import Array
from numpy import array as npArray, uint8 

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
    
  newImage = amogussify(image)

  imageio.imwrite(destImagePath, newImage)


def amogussify(rawImageMatrix: Array):
  convertedRowList = []
  i = 0

  for row in rawImageMatrix:
    print("Processing row #", i)
    convertedRowList.extend(amogussifyRow(row))
    i += 1

  return Array(npArray(convertedRowList))


def amogussifyRow(rawRow: Array):
  convertedPixelList = []

  for rawPixel in rawRow:
    convertedPixelList.append(amogussifyPixel(rawPixel))
  
  marchedPixelList = [[], [], [], []]

  for convertedPixel in convertedPixelList:
    for i in range (4):
      marchedPixelList[i].extend(convertedPixel[i])
      
  return Array(npArray(marchedPixelList))


def amogussifyPixel(rawPixel: Array):

  r = rawPixel[0]
  g = rawPixel[1]
  b = rawPixel[2]
  a = rawPixel[3] if len(rawPixel) == 4 else 255

  rRev = uint8(255 if r > 170 else r*1.5)
  gRev = uint8(255 if g > 170 else g*1.5)
  bRev = uint8(255 if b > 170 else b*1.5)

  pixelOrig = [r, g, b, a]
  pixelRev = [rRev, gRev, bRev, a]

  newAmogus = npArray([
    [pixelOrig, pixelOrig, pixelOrig, pixelRev],
    [pixelOrig, pixelRev, pixelOrig, pixelOrig],
    [pixelOrig, pixelOrig, pixelOrig, pixelOrig],
    [pixelOrig, pixelRev, pixelOrig, pixelRev],
  ])

  return Array(newAmogus)

main()