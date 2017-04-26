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
from PIL import Image, ImageFilter
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
    data.taggedImages = 0
    data.untaggedImages = 0
    data.readyToGo = False
    data.untaggedImagesList = []


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
    canvas.create_image(data.width//2+buttonOffsetRight,data.height//2+buttonOffsetDown, image=data.introButtonImage)

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
            I have created the backend infrastructure that will process your images and data, to cut 
            the conceptually difficult parts out of the process. In fact, you could probably pay your eleven year-
            old cousin to do it for you. 

            Disclaimer: Gathering and tagging data is still a long process, and will require you to write hundreds of
            sentences on a whiteboard. Also, CalliGraphics does not condone child labor."""
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text)
    canvas.create_image(data.width//2,data.height//2+buttonOffsetDown, image=data.challengeButtonImage)

def redrawAllUpload(canvas,data):
    borderTop = 30
    borderLeft = 55
    borderBottom = 470
    borderRight = 945
    buttonOffsetDown = 150
    text = """First, write out the first 50 digits of Pi in one image.
            For reference, these are:
            3.1415926535897932384626433832795028841971693993751 
            Upload your photo here:"""
    canvas.create_image(data.width//2,data.height//2, image=data.borderImage)
    canvas.create_rectangle(borderLeft,borderTop,borderRight,borderBottom, fill="white", width=0)
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text)
    canvas.create_image(data.width//2,data.height//2+.5*buttonOffsetDown, image=data.uploadButtonImage)
    if data.readyToGo == True:
            canvas.create_image(data.width//2,data.height//2+buttonOffsetDown, image=data.tagButtonImage)

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
    canvas.create_text(data.width//2,data.height//2,anchor=S,text=text)

def redrawAllDone(canvas,data):
    pass


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
    if event.y > uploadButtonTop and event.y < uploadButtonBottom:
        if event.x > uploadButtonLeft and event.x < uploadButtonRight:
            openFiles()
            countFilesInUntagged(data)
            loadFilesIntoData(data)

def loadFilesIntoData(data):
    for fileNumber in range(data.untaggedData):
        data.untaggedImagesList.append(PhotoImage("characterData/untaggedData/%d.jpg"%fileNumber))

def openFiles():
    unparsedImage = askopenfilenames()
    imageDetectionAndParsing(unparsedImage[0])

def countFilesInUntagged(data):
    data.untaggedData = len([name for name in os.listdir(
                            'characterData/untaggedData') if os.path.isfile('characterData/untaggedData/' + name)])
    data.readyToGo = True

def mousePressedTag(event,data):
    pass

def mousePressedDone(event,data):
    pass
    

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
        return ("tag = " + str(self.tag) + str(vec))

run(1000, 500)

print(trainingVectors.instances)