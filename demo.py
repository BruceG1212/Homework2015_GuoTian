from PIL import Image
from pylab import *
from array import array
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np
import os
import math
import easygui

im = Image.open('./chess.png').convert('L')
plt.xlim(0,206)
plt.ylim(0,180)
imshow(im)
gray()
hold('on')

easygui.msgbox("Please select Target point: ")
x = ginput(1)
print 'you clicked:',x
xval,yval = x[0]
xval = int(xval)
yval = int(yval)
print(xval,yval)
show()
