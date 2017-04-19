#UserInterface by Elizabeth Viera
#Graphics largely created in Adobe Illustrator. Main logo stock image from Adobe, with alterations by me.
#Button images created using http://dabuttonfactory.com
#images starter file used from 112 website

from tkinter import *

####################################
# customize these functions
####################################

####################################
#Init and Mode Control
####################################
def init(data):
    data.mode = "Introduction"
    data.introImage = PhotoImage(file="tkinterimages/MainPageLogo.png")
    data.introButtonImage = PhotoImage(file="tkinterimages/button.jpg")
    data.borderImage = PhotoImage(file="tkinterimages/borderGradient.png")
    data.challengeButtonImage = PhotoImage(file="tkinterimages/AcceptChallengeButton.jpg")

def redrawAll(canvas, data):
    if data.mode == "Introduction":
        redrawAllIntro(canvas,data)
    elif data.mode == "Directions":
        redrawAllDirection(canvas,data)
    else:
        pass

def mousePressed(event, data):
    if data.mode == "Introduction":
        mousePressedIntro(event,data)
    elif data.mode == "Directions":
        mousePressedDirection(event,data)
    else:
        pass

def keyPressed(event, data): 
    if data.mode == "Introduction":
        keyPressedIntro(event,data)
    elif data.mode == "Direction":
        keyPressedDirection(event,data)
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

##############################################
#Key Pressed Functions
##############################################
def keyPressedIntro(event,data):
    pass

def keyPressedDirection(event,data):
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

run(1000, 500)
