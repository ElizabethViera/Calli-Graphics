#Elizabeth Viera, using Pillow
from __future__ import print_function
from PIL import Image, ImageFilter
from CalliGraphicsImageTagging import *

def imageDetectionAndParsing(string): 
    imageWidth = 408
    imageHeight = 300
    imagePath = string
    image = Image.open(string)
    image = outlineMarks(image, imageWidth, imageHeight)
    imageData = partitionCharacters(image)
    imageFragments = createNewCharacterImages(imageData)
    pushToFile(imageFragments)

def imagePredict(string):
    imageWidth = 408
    imageHeight = 300
    imagePath = string
    image = Image.open(string)
    image = outlineMarks(image, imageWidth, imageHeight)
    imageData = partitionCharacters(image)
    imageFragments = createNewCharacterImages(imageData)
    assignedData = assignVectors(imageFragments)
    return assignedData

def assignVectors(imageFragments): #takes in list of images
    assignedVecs = []
    for fragment in imageFragments:
        assignedVecs.append(predictCharacter(fragment))
    return assignedVecs

def outlineMarks(image, imageWidth, imageHeight):
    def colorsAreVeryDifferent(color1,color2):
        r1,g1,b1 = color1[0], color1[1], color1[2]
        r2,g2,b2 = color2[0], color2[1], color2[2]
        if (r1-r2 > 15 or g1-g2 > 15 or b1-b2 > 15):
            return True
        return False

    image = image.resize((imageWidth, imageHeight), Image.BICUBIC) 
    maxPass = image.filter(ImageFilter.RankFilter(13,99)) #radius 13
    for x in range(image.size[0]):
        for y in range(image.size[1]):
            currentColor = image.getpixel((x,y))
            maxPassColor = maxPass.getpixel((x,y)) 
            #Compare current pixel with locally brightest thing
            if(colorsAreVeryDifferent(maxPassColor,currentColor)):
                image.putpixel((x,y),(0,255,0)) #make pixel very green
            else: 
                image.putpixel((x,y),(255,255,255))    
    return image

def partitionCharacters(image):
    def floodFill(Startx, Starty, count):
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

    imageValues = [[-1 for y in range(image.size[1])] \
                    for x in range(image.size[0])]
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
                subPartition, imageValues = floodFill(x, y, count)
                if len(subPartition) > 20:
                    partitions.append(subPartition)
    return partitions

def createNewCharacterImages(imageData):
    imageFragments = []
    imageDimensions = []
    for image in imageData:
        #This function will find the dimensions of each image fragment
        minRow, maxRow, minCol, maxCol = None, None, None, None
        for (x,y) in image:
            if (minRow == None or maxRow == None or 
                minCol == None or maxCol == None):
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
    for imageIndex in range(len(imageDimensions)):
        #This will create an image of the fragment
        newImageHeight = imageDimensions[imageIndex][0]
        newImageWidth = imageDimensions[imageIndex][1]
        imagePadding = 1
        newImageSquare = max(newImageWidth,newImageHeight)+imagePadding
        centerAmount, widthOrHeight = calculateCentering(newImageHeight,
                                                         newImageWidth)
        fragment = Image.new('RGB', (newImageSquare, newImageSquare), 
                             color=(255,255,255))
        for (x,y) in imageData[imageIndex]:
            if widthOrHeight == "Height":
                x = x-imageDimensions[imageIndex][2] + centerAmount
                y = y-imageDimensions[imageIndex][3]
            else:
                x = x-imageDimensions[imageIndex][2]
                y = y-imageDimensions[imageIndex][3] + centerAmount
            fragment.putpixel((x,y),(115,109,198))
            #fragment.show()
        finalWidth = 30
        finalHeight = 30
        fragment = fragment.resize((finalWidth, finalHeight), Image.BICUBIC)
        newImages.append(fragment)
        #fragment.show()
    return newImages

def calculateCentering(Height,Width):
    maxLength = max(Height,Width) 
    centerAmount = abs(Height-Width)//2
    if maxLength == Height:
        return centerAmount, "Width"
    else:
        return centerAmount, "Height"

def pushToFile(listOfImages):
    count = 0
    for image in listOfImages:    
        image.save("characterData" + "\\" + "untaggedData" 
                    + "\\" + "%d.jpg" % count)
        count += 1
