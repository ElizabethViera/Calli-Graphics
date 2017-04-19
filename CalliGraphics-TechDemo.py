#Elizabeth Viera, svierapa
#CalliGraphics-Numpy and SciKitLearn Demo
import numpy as np 
import scipy as sp 
import sklearn as skl 

def numpyDemo():
    c = [1,.5,.3,.2,.9,9]
    d = [1,.6,.8,.3,.1,10]
    #it is VERY IMPORTANT that 1d lists not be modified after creating the arrays
    a = np.array(c) #in my project, data will be stored like this
    b = np.array(d) 
    return a+b
