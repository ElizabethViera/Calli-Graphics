#Elizabeth Viera, svierapa
#Tagging Data
#Stack Overflow cite: http://stackoverflow.com/questions/1401712/how-can-the-
#euclidean-distance-be-calculated-with-numpy

import numpy as np 
from PIL import Image, ImageFilter

def maxSelf():
    Zero = [25,28]
    One = [4,8,19,21,23]
    Two = [2,31,36,41,44]
    Three = [0,5,34,35,37,40,47,51,53]
    Four = [1,12,27,50]
    print("Zero to zero:", distanceFunction(25,28))
    print("Three to Three:")
    Threes = []
    for i in range (len(Three)):
        for j in range(i+1,len(Three)):
            dist = distanceFunction(Three[i],Three[j])
            Threes.append([dist,Three[i],Three[j]])
    Threes = max(Threes)
    print(Threes)
    print ("Three to Other:")
    ThreeOther = []
    for i in range(len(Three)):
        for j in range(53):
            if j in Three: continue
            else:
                dist = distanceFunction(Three[i],j)
                ThreeOther.append([dist,Three[i],j])
    print (min(ThreeOther))


def distanceFunction(vectorOne,vectorTwo): #ints
    arrayOne = analyzeCharacter(vectorOne)
    arrayTwo = analyzeCharacter(vectorTwo)
    dist = np.linalg.norm(arrayOne-arrayTwo) #stackOverflowDistance
    return dist

def analyzeCharacter(n):
    imageToTag, comparisonImages = getImages(n)
    vectors = makeVectors(imageToTag,comparisonImages)
    singleVector = flattenVector(vectors)
    array = np.array(singleVector)
    return array

def flattenVector(vectors):
    result = []
    for vector in vectors:
        for entry in vector:
            result.append(entry)
    return result

def makeVectors(imageToTag,comparisonImages):
    vectorTopLeft = compareTopLeft(imageToTag,comparisonImages)
    vectorTopMid = compareTopMid(imageToTag,comparisonImages)
    vectorTopRight = compareTopRight(imageToTag,comparisonImages)
    vectorMidLeft = compareMidLeft(imageToTag,comparisonImages)
    vectorMidMid = compareMidMid(imageToTag,comparisonImages)
    vectorMidRight = compareMidRight(imageToTag,comparisonImages)
    vectorLowLeft = compareLowLeft(imageToTag,comparisonImages)
    vectorLowMid = compareLowMid(imageToTag,comparisonImages)
    vectorLowRight = compareLowRight(imageToTag,comparisonImages)
    return [vectorTopLeft,vectorTopMid,vectorTopRight,
            vectorMidLeft,vectorMidMid,vectorMidRight,
            vectorLowLeft,vectorLowMid,vectorLowRight]
    

def getImages(n):
    imageToTag = Image.open("CharacterData/untaggedData/%d.jpg" % n)
    leftHalf = Image.open("VectorImageComparisons/LeftHalf.png")
    middleLineHorizontal = Image.open(
                            "VectorImageComparisons/MiddleLineHorizontal.png")
    middleLineVertical = Image.open(
                            "VectorImageComparisons/MiddleLineVertical.png")
    topHalf = Image.open("VectorImageComparisons/TopHalf.png")
    topLeftDiagonal = Image.open("VectorImageComparisons/TopLeftDiagonal.png")
    topRightDiagonal = Image.open("VectorImageComparisons/TopRightDiagonal.png")
    return imageToTag, [leftHalf,middleLineHorizontal,middleLineVertical,
                        topHalf,topLeftDiagonal,topRightDiagonal]

def compareTopLeft(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row,col)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareTopMid(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row,col+10)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareTopRight(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row,col+20)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareMidLeft(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+10,col)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareMidMid(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+10,col+10)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareMidRight(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+10,col+20)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareLowLeft(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+20,col)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareLowMid(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+20,col+10)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector

def compareLowRight(imageToTag,comparisonImages):
    comparisonPixels = 10
    comparisonVector = []
    for comparison in comparisonImages: #comparison is an image
        similarityPercent = 0
        for row in range(comparisonPixels): #number of pixels in comparison
            for col in range(comparisonPixels):
                if (imageToTag.getpixel((row+20,col+20)) == 
                    comparison.getpixel((row,col))):
                    similarityPercent += 1
        comparisonVector.append(similarityPercent)
    return comparisonVector