readme.txt

My project allows the user to upload a photo of digits they wrote on a whiteboard and tag the images with a clean, easy-to-use interface.
Then, the user can upload a new photo of text. The program uses the aquired data to make predictions of the letters contained in the file.

This was built using tkinter (built into Python), tkinter.filedialog (built into Python),PIL, numpy, os (built into Python), and os.path (built into Python). 

Numpy can be accessed via http://www.numpy.org/.

PIL can be accessed via https://pillow.readthedocs.io/en/4.1.x/.

To run the program (when you have the correct libraries installed), open CalliGraphicsUserInterface.py and verify that the other two python files (Image Tagging and Image Detection) are in the same directory. Additionally, tkinterImages and CharacterData need to be preserved, with an empty folder in CharacterData named "untaggedData". 

You may put jpg files in TestCases if you would like, but the program can run them from anywhere so long as they are saved on your computer.

Digits to be recognized should be connected and discrete. The program requires around two minutes to process data to make a prediction: this time will increase as you do multiple passes of training data. 

This should be all information you need to run CalliGraphics. 