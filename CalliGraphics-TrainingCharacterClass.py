#Elizabeth Viera
#Training Character Class
class TrainingCharacter(object):
    def __init__(image):
        self.image = image
        self.character = None #unassigned

    def label(self,event):
        self.character = event.keyPress

    def __repr__(image):
        return self.character