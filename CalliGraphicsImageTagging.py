#Elizabeth Viera, svierapa
#Tagging Data
#Stack Overflow cite: http://stackoverflow.com/questions/1401712/how-can-the-
#euclidean-distance-be-calculated-with-numpy
#PCA implemented with Smith, Lindsay J. 'A tutorial on Principal Components Analyses' 2002, PDF.
#Methodology similar to Eigenfaces, as directed in https://en.wikipedia.org/wiki/Eigenface

import numpy as np 
from PIL import Image, ImageFilter

def distanceFunction(vectorOne,vectorTwo): 
    vectorOne = np.array(vectorOne)
    vectorTwo = np.array(vectorTwo)
    dist = np.linalg.norm(vectorOne-vectorTwo) #stackOverflowDistance
    return dist

def predictCharacter(fragment):
    imageToTag, comparisonImages = fragment, predictGetImages()
    vectors = makeVectors(imageToTag,comparisonImages)
    singleVector = flattenVector(vectors)
    array = np.array(singleVector)
    return array

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
    
def predictGetImages():
    leftHalf = Image.open("VectorImageComparisons/LeftHalf.png")
    middleLineHorizontal = Image.open(
                            "VectorImageComparisons/MiddleLineHorizontal.png")
    middleLineVertical = Image.open(
                            "VectorImageComparisons/MiddleLineVertical.png")
    topHalf = Image.open("VectorImageComparisons/TopHalf.png")
    topLeftDiagonal = Image.open("VectorImageComparisons/TopLeftDiagonal.png")
    topRightDiagonal = Image.open("VectorImageComparisons/TopRightDiagonal.png")
    return [leftHalf,middleLineHorizontal,middleLineVertical,
                        topHalf,topLeftDiagonal,topRightDiagonal]

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

#####################################################
#Basically EigenFaces
#####################################################


#####################################################
#PCA Implementation
#####################################################

def PCAOfVectors(vectorList):
    newDataSet, arithmeticMean = subtractArithmeticMean(vectorList)
    covarianceMatrix = createCovarianceMatrix(newDataSet)
    eigenVectors = findEigenVectors(covarianceMatrix)
    return eigenVectors, arithmeticMean

def findEigenVectors(matrix):
    eigenVectors = []
    for eigenVector in range(len(matrix)):
        eigenVector = getEigenValuesOfCovariance(matrix,eigenVectors)
        eigenVectors.append(eigenVector)
        matrix -= np.dot(np.dot(matrix,eigenVector),eigenVector)
    return eigenVectors


def subtractArithmeticMean(vectorList):
    numberOfVectors = len(vectorList)
    if numberOfVectors != 0:
        vectorScalar = 1/numberOfVectors
    else:
        vectorScalar = 0
    vectorLength = vectorList[0].size
    totalVector = [0 for entry in range(vectorLength)]
    totalVector = np.array(totalVector)
    for vector in vectorList:
        totalVector = totalVector + vector
    arithmeticMean = totalVector*vectorScalar
    arithmeticMean = np.array(arithmeticMean)
    adjustedVectorList = []
    for vector in vectorList:
        adjustedVector = vector-arithmeticMean
        adjustedVectorList.append(adjustedVector)
    return adjustedVectorList, arithmeticMean

def createCovarianceMatrix(newDataSet):
    numberOfVectors = len(newDataSet)
    if numberOfVectors != 1:
        covarianceScalar = 1/(numberOfVectors-1)
    else: 
        covarianceScalar = 0
    vectorLength = newDataSet[0].size
    covarianceMatrix = [[0 for col in range(vectorLength)] for row in range(vectorLength)]
    for row in range(len(covarianceMatrix)):
        for col in range(len(covarianceMatrix[0])):
            totalSum = 0
            for i in range(numberOfVectors):
                totalSum += newDataSet[i][row]*newDataSet[i][col]
            covarianceMatrix[row][col] = totalSum/numberOfVectors
    covarianceMatrix = np.array(covarianceMatrix)
    return covarianceMatrix*covarianceScalar

def getEigenValuesOfCovariance(matrix,eigenVectors): #2dLists
    #Power Iteration
    #takes in nxn matrix and a possibly empty list of eigenVectors
    vectorDimension = len(matrix) #n
    uVec = np.random.rand(vectorDimension)
    for i in range(1,1000): 
        uVec = np.dot(matrix,uVec)
        if eigenVectors != []:
            uVec = projectOut(uVec,eigenVectors)
        norm=np.linalg.norm(uVec)
        uVec = uVec/norm
    return uVec

def projectOut(vector,eigenVectors):
    for eigenVector in eigenVectors:
        vector = vector - np.dot(np.dot(vector,eigenVector),eigenVector)
    return vector 

###################################################
#TestFunctions
###################################################
def PCATest():
    print("Testing Arithmetic Mean. . . ")
    a = [0,1,2,3,4]
    b = [2,3,4,5,6]
    c = [1,2,1,1,1]
    d = [0,1,2,3,9]
    testA = np.array(a)
    testB = np.array(b)
    testC = np.array(c)
    testD = np.array(d)
    listOfArrays = [testA, testB, testC, testD]
    #Test from pdf, page 13:
    e = [2.5,2.4]
    f = [.5,.7]
    g = [2.2,2.9]
    h = [1.9,2.2]
    i = [3.1,3.0]
    j = [2.3,2.7]
    k = [2,1.6]
    l = [1,1.1]
    m = [1.5,1.6]
    n = [1.1,.9]
    testE = np.array(e)
    testF = np.array(f)
    testG = np.array(g)
    testH = np.array(h)
    testI = np.array(i)
    testJ = np.array(j)
    testK = np.array(k)
    testL = np.array(l)
    testM = np.array(m)
    testN = np.array(n)
    listOfData = [testE,testF,testG,testH,testI,testJ,testK,testL,testM,testN]
    #print(subtractArithmeticMean(listOfData))
    print(PCAOfVectors(listOfData))
    print("Passed!")






#####################################################
#test function for ML callibration
#####################################################

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

