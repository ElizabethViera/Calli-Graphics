#Elizabeth Viera, using Pillow
from __future__ import print_function
from PIL import Image, ImageFilter



def main():
    imageWidth = 408
    imageHeight = 300
    image = Image.open("edgeDetectionCases11.jpg")
    image = pixelMethods(image, imageWidth, imageHeight)
    imageData = assignNumbers(image)
    imageFragments = backToImages(imageData)
    

def pixelMethods(image, imageWidth, imageHeight):
    image = image.resize((imageWidth, imageHeight), Image.BICUBIC) 
    #image.show()
    maxPass = image.filter(ImageFilter.RankFilter(13,99)) #radius 13
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            currentColor = image.getpixel((x,y))
            maxPassColor = maxPass.getpixel((x,y)) #Compare current pixel with locally brightest thing
            if(colorsAreVeryDifferent(maxPassColor,currentColor)):
                image.putpixel((x,y),(0,255,0)) #make pixel very green
            else: 
                image.putpixel((x,y),(255,255,255))
    image.show()        
    return image

def colorsAreVeryDifferent(color1,color2):
    r1,g1,b1 = color1[0], color1[1], color1[2]
    r2,g2,b2 = color2[0], color2[1], color2[2]
    if (r1-r2 > 15 or g1-g2 > 15 or b1-b2 > 15):
        return True
    return False

def assignNumbers(image):
    imageValues = [[-1 for y in range(image.size[1])] for x in range(image.size[0])]
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if image.getpixel((x,y)) == (0,255,0):
                imageValues[x][y] = 0
    count = 0
    partitions = []
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            if imageValues[x][y] == 0:
                count += 1
                imageValues[x][y] = count
                subPartition, imageValues = floodFill(imageValues, x, y, count)
                if len(subPartition) > 20:
                    partitions.append(subPartition)
    return partitions
                
def floodFill(imageValues, Startx, Starty, count):
    subPartition = [(Startx,Starty)]
    for x,y in subPartition:
        for z in range(-1,2):
            for w in range(-1,2):
                if not (x+z < 0 or y+w < 0 or x+z >= len(imageValues) 
                    or y+w >= len(imageValues[0])):
                    if imageValues[x+z][y+w] == 0:
                        imageValues[x+z][y+w] = count
                        subPartition.append((x+z,y+w))
    return subPartition, imageValues

def backToImages(imageData):
    imageFragments = []
    imageDimensions = []
    for image in imageData:
        #This function will find the dimensions of each image fragment
        minRow, maxRow, minCol, maxCol = None, None, None, None
        for (x,y) in image:
            if minRow == None or maxRow == None or minCol == None or maxCol == None:
                minRow = x
                maxRow = x
                minCol = y
                maxCol = y
            else: 
                if x < minRow:
                    minRow = x
                if x > maxRow:
                    maxRow = x
                if y < minCol:
                    minCol = y
                if y > maxCol:
                    maxCol = y
        imageDimensions.append((maxRow-minRow,maxCol-minCol,minRow,minCol))
    newImages = []
    for newImage in range(len(imageDimensions)):
        #This will create an image of the fragment
        newImageHeight = imageDimensions[newImage][0]
        newImageWidth = imageDimensions[newImage][1]
        fragment = Image.new('RGB', (newImageHeight+10, newImageWidth+10), color=(255,255,255))
        for (x,y) in imageData[newImage]:
            print(x,y)
            x = x-imageDimensions[newImage][2]
            y = y-imageDimensions[newImage][3]
            print(x,y,fragment.size,imageDimensions)
            fragment.putpixel((x,y),(115,109,198))
            #fragment.show()
        newImages.append(fragment)
        fragment.show()

    #print data onto newImages
    return newImages



