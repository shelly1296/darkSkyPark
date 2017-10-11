
# coding: utf-8

# In[2]:

# Python version
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

# In addition to the online example, these packages below help dealinf with the file system
import glob
import os
from PIL import Image


# In[7]:

## Part 1: Lets do a loop


# In[4]:

# Load libraries
import pandas
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from datetime import date


# In[5]:

dir = r'C:\Users\Adam Shelbourne\Uni\Physics\Astr310\Python\mu\daily\*'
names = ['UTCDateTime', 'LocalDateTime', 'Temperature', 'Counts', 'Frequency', 'MSAS']


# In[9]:

# Set the common time grid onto which each night is sampled. The common grid 
# is defined by the start time defined below, and the number of hours from that time
beginh = 16 # Hour of start time (hour)
beginm = 30 # Hour of start time (minute)
nhrs = 15   # Number of hours to extend time grid

#print  (glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat'))

numbfile = len(glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat'))
print (numbfile)


# In[8]:

for infile in sorted(glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat')):
   print (infile[69:77])


# In[ ]:



