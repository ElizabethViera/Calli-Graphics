#UserInterface by Elizabeth Viera
#Graphics largely created in Adobe Illustrator. Main logo stock image from Adobe, with alterations by me.
#Button images created using http://dabuttonfactory.com
#images starter file used from 112 website
#https://tkinter.unpythonic.net/wiki/tkFileDialog for dialogue boxes, assisted by TA Ahbi
#stack Overflow citation http://stackoverflow.com/questions/9239514/filedialog-tkinter-and-opening-files
#stack Overflow citation 

from tkinter import *
from tkinter.filedialog import askopenfilenames 
from CalliGraphicsImageTagging import *
from CalliGraphicsImageDetection import *
from PIL import Image, ImageFilter, ImageTk
import os, os.path

####################################
# customize these functions
####################################

####################################
#Init and Mode Control
####################################
def init(data):
    data.mode = "Introduction"
    data.introImage = PhotoImage(file="tkinterimages/MainPageLogo.png")
    data.introButtonImage = PhotoImage(file="tkinterimages/directions.jpg")
    data.borderImage = PhotoImage(file="tkinterimages/borderGradient.png")
    data.challengeButtonImage = PhotoImage(file="tkinterimages/AcceptChallengeButton.jpg")
    data.tagButtonImage = PhotoImage(file="tkinterimages/tagYourImages.jpg")
    data.uploadButtonImage = PhotoImage(file="tkinterimages/uploadYourImages.jpg")
    data.trainMoreImage = PhotoImage(file="tkinterimages/trainMoreData.jpg")
    data.imageProcessingImage = ImageTk.PhotoImage(file="tkinterimages/LoadingScreen.png")
    data.taggedImages = 0
    data.untaggedImages = 0
    data.readyToGo = False
    data.untaggedImagesList = []
    data.predictionFile = ""
    data.imageProcessing = False

def redrawAll(canvas, data):
    if data.mode == "Introduction":
        redrawAllIntro(canvas,data)
    elif data.mode == "Directions":
        redrawAllDirection(canvas,data)
    elif data.mode == "UploadWhiteboardPhotos":
        redrawAllUpload(canvas,data)
    elif data.mode == "Tag":
        redrawAllTag(canvas,data)
    elif data.mode == "Done!":
        redrawAllDone(canvas,data)
    else:
        pass

def mousePressed(event, data):
    if data.mode == "Introduction":
        mousePressedIntro(event,data)
    elif data.mode == "Directions":
        mousePressedDirection(event,data)
    elif data.mode == "UploadWhiteboardPhotos":
        mousePressedUpload(event,data)
    elif data.mode == "Tag":
        mousePressedTag(event,data)
    elif data.mode == "Done!":
        mousePressedDone(event,data)
    else:
        pass

def keyPressed(event, data): 
    if data.mode == "Introduction":
        keyPressedIntro(event,data)
    elif data.mode == "Direction":
        keyPressedDirection(event,data)
    elif data.mode == "UploadWhiteboardPhotos":
        keyPressedUpload(event,data)
    elif data.mode == "Tag":
        keyPressedTag(event,data)
    elif data.mode == "Done!":
        keyPressedDone(event,data)
    else: 
        pass

def timerFired(data):
    pass #never use timer

##############################################
#redraw functions
##############################################
def redrawAllIntro(canvas,data):
    buttonOffsetDown = 200
    buttonOffsetRight = 20
    canvas.create_image(data.width//2,data.height//2, image=data.introImage)
    canvas.create_image(data.width//2+buttonOffsetRight,
            data.height//2+buttonOffsetDown, image=data.introButtonImage)

def redrawAllDirection(canvas,data):
    borderTop = 30
    borderLeft = 55
    borderBottom = 470
    borderRight = 945
    buttonOffsetDown = 150
    text = """
            Digit and character recognition are hard problems. This project 
            streamlines the process of creating a module that allows you to turn your whiteboard handwriting into 
            a textfile using an automated process. The task left to you is to write out some data and tag it! 
            I have created the structures that will process your images and data. This cuts 
            the conceptually difficult parts out of the process! In fact, you could probably pay your eleven year-
            old cousin to do it for you.

            Disclaimer: Gathering and tagging data is still a long process, and will require you to write hundreds of
            numbers on a whiteboard. Also, CalliGraphics does not condone child labor."""
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text, font="Times 12")
    canvas.create_image(data.width//2,data.height//2+buttonOffsetDown, image=data.challengeButtonImage)

def redrawAllUpload(canvas,data):
    borderTop = 30
    borderLeft = 55
    borderBottom = 470
    borderRight = 945
    buttonOffsetDown = 150
    text = """Write out a large number of numbers, preferable in a mixed order. 
            (For example, the first 50 digits of Pi:
            3.1415926535897932384626433832795028841971693993751) 
            Upload your photo here:"""
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text, font="Times 12")
    canvas.create_image(data.width//2,data.height//2+.5*buttonOffsetDown, image=data.uploadButtonImage)
    if data.readyToGo == True:
        canvas.create_image(data.width//2,data.height//2+buttonOffsetDown, image=data.tagButtonImage)
    if data.imageProcessing == True:
        canvas.create_image(data.width//2,data.height//2, image=data.imageProcessingImage)

def redrawAllTag(canvas,data):
    borderTop = 30
    borderLeft = 55
    borderBottom = 470
    borderRight = 945
    buttonOffsetDown = 150
    characterOffsetUp = 32
    text = "What is this a picture of? (Please press a key to tell me, or 'Delete' if this isn't a character. Oops!)"
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    currentCharacter = data.untaggedImagesList[data.taggedImages] #data.taggedImages is an int
    canvas.create_image(data.width//2,data.height//2-characterOffsetUp, image=currentCharacter)
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text, font="Times 12")

def redrawAllDone(canvas,data):
    borderTop = 30
    borderLeft = 55
    borderBottom = 470
    borderRight = 945
    buttonOffsetDown = 150
    resultOffset = 30
    text = "Congrats! You're all done tagging your data! Upload a photo of numbers to convert it to text!"
    resultText = "Your result: " + data.predictionFile
    moreTrainingText = "Not quite right? Click below to train with more data!"
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    canvas.create_text(data.width//2,data.height//2-resultOffset,anchor=S,text=text, font="Times 12")
    if data.predictionFile != "":
        canvas.create_text(data.width//2,data.height//2,anchor=S,text=resultText, font="Times 12")
        canvas.create_text(data.width//2,data.height//2+resultOffset, anchor=S,text=moreTrainingText, font="Times 12")
        canvas.create_image(data.width//2,data.height//2+buttonOffsetDown, image=data.trainMoreImage)
    canvas.create_image(data.width//2,data.height//2+.5*buttonOffsetDown, image=data.uploadButtonImage)


##############################################
#mousePressed Functions
##############################################
def mousePressedIntro(event,data):
    buttonTop = 438
    buttonBottom = 460
    buttonLeft = 425
    buttonRight = 615
    if event.y > buttonTop and event.y < buttonBottom:
        if event.x > buttonLeft and event.x < buttonRight:
            data.mode = "Directions"

def mousePressedDirection(event,data):
    buttonTop = 380
    buttonBottom = 410
    buttonLeft = 380
    buttonRight = 620
    if event.y > buttonTop and event.y < buttonBottom:
        if event.x > buttonLeft and event.x < buttonRight:
            data.mode = "UploadWhiteboardPhotos"

def mousePressedUpload(event,data):
    #button dimensions, next
    #upload stuffs
    buttonTop = 385
    buttonBottom = 412
    buttonLeft = 405
    buttonRight = 595
    uploadButtonTop = 310
    uploadButtonBottom = 340
    uploadButtonLeft = 405
    uploadButtonRight = 600
    if event.y > buttonTop and event.y < buttonBottom:
        if event.x > buttonLeft and event.x < buttonRight:
            if data.readyToGo == True:
                data.mode = "Tag"
                data.readyToGo = False
            #reset in case training additional later
    if event.y > uploadButtonTop and event.y < uploadButtonBottom:
        if event.x > uploadButtonLeft and event.x < uploadButtonRight:
            data.imageProcessing = True
            openFiles()
            countFilesInUntagged(data)
            loadFilesIntoData(data)
            data.imageProcessing = False


def loadFilesIntoData(data):
    for fileNumber in range(data.untaggedData):
        data.untaggedImagesList.append(ImageTk.PhotoImage(file="characterData/untaggedData/%d.jpg"%fileNumber))

def openFiles():
    unparsedImage = askopenfilenames()
    imageDetectionAndParsing(unparsedImage[0])

def countFilesInUntagged(data):
    data.untaggedData = len([name for name in os.listdir(
                            'characterData/untaggedData') if os.path.isfile('characterData/untaggedData/' + name)])
    data.readyToGo = True

def mousePressedTag(event,data):
    pass

def predictFile(data):
    predictImage = askopenfilenames()
    assignedData = imagePredict(predictImage[0]) #list of vectors
    predictionFile = []
    #Compile Training Data into a matrix, transpose, run through PCA, create Basis.
    #Get image in terms of basis, make prediction
    trainingDataMatrix = []
    for instance in trainingVectors.instances:
        newVector = np.array(instance.vec)
        trainingDataMatrix.append(newVector)
    eigenbasisOfData, arithmeticMean = PCAOfVectors(trainingDataMatrix)
    #This created the eigenbasis. So the old data has to be projected through again.
    for instance in trainingVectors.instances:
        instance.pvec = np.array(projectionFunction(instance.vec,eigenbasisOfData,arithmeticMean))
    #then we go through each data vector, project it into the space, and find the closest instance to it
    for imageData in assignedData:
        #Project into eigenbasis of Data
        projection = projectionFunction(imageData, eigenbasisOfData,arithmeticMean)
        #make prediction
        predictedTag = closestNeighbor(projection)
        predictionFile.append(predictedTag)
    for number in predictionFile:
        data.predictionFile += number

def closestNeighbor(projection):
    minimum = None
    for instance in trainingVectors.instances:
        distance = distanceFunction(projection,instance.pvec)
        if minimum == None:
            minimum = distance
            tag = instance.tag 
        else:
            if minimum > distance:
                minimum = distance
                tag = instance.tag
    return tag

def projectionFunction(vector,eigenbasis,arithmeticMean):
    projection = []
    vector = vector-arithmeticMean
    for eigenvector in eigenbasis:
        dotProduct = np.dot(vector, eigenvector)
        projection.append([dotProduct])
    return projection

def mousePressedDone(event,data):
    uploadButtonTop = 310
    uploadButtonBottom = 335
    uploadButtonLeft = 405
    uploadButtonRight = 600
    trainMoreButtonTop = 385
    trainMoreButtonBottom = 410
    trainMoreButtonLeft = 400
    trainMoreButtonRight = 600
    if event.y > uploadButtonTop and event.y < uploadButtonBottom:
        if event.x > uploadButtonLeft and event.x < uploadButtonRight:
            predictFile(data)
    if data.predictionFile != "":
        if event.y > trainMoreButtonTop and event.y < trainMoreButtonBottom:
            if event.x > trainMoreButtonLeft and event.x < trainMoreButtonRight:
                data.mode = "UploadWhiteboardPhotos"
                data.taggedImages = 0
                data.untaggedImages = 0
            
    

##############################################
#Key Pressed Functions
##############################################
def keyPressedIntro(event,data):
    pass

def keyPressedDirection(event,data):
    pass

def keyPressedUpload(event,data):
    pass

def keyPressedTag(event,data):
    if event.keysym == "Delete":
        data.taggedImages += 1
    elif event.keysym.isdigit():
        thisVector = analyzeCharacter(data.taggedImages)
        trainingVectors(thisVector,event.keysym)
        data.taggedImages += 1
    if data.taggedImages == data.untaggedData:
        data.mode = "Done!"
        for file in os.listdir("CharacterData/untaggedData"):
            os.remove("CharacterData/untaggedData/" + file)
        #empty folder so that the next time this program is run, you don't get interference
        #Also, so that the user may submit more data if they want
    
def keyPressedDone(event,data):
    pass


####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds

    # create the root and the canvas (Note Change: do this BEFORE calling init!)
    root = Tk()

    init(data)
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

class trainingVectors(object):
    instances = []
    def __init__(self,vec,tag):
        self.vec = vec
        self.tag = tag
        trainingVectors.instances.append(self)
    def __repr__(self):
        return (str(self.tag) + " " + str(self.vec))

run(1000, 500)

