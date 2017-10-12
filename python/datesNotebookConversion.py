
# coding: utf-8

# In[5]:

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


# In[7]:

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
import sys


# In[3]:

dir = 'C:\Users\Adam Shelbourne\Uni\Physics\Astr310\Python\mu\daily\*'
names = ['UTCDateTime', 'LocalDateTime', 'Temperature', 'Counts', 'Frequency', 'MSAS']
print(glob.glob(dir))


# In[9]:

# Set the common time grid onto which each night is sampled. The common grid 
# is defined by the start time defined below, and the number of hours from that time
beginh = 16 # Hour of start time (hour)
beginm = 30 # Hour of start time (minute)
nhrs = 15   # Number of hours to extend time grid

#print  (glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat'))

numbfile = len(glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat'))
print (numbfile)


# In[43]:

javascript= r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\graph\\darkskiesdata.js'
f2=open(javascript,'w')
#Write Header first 7 lines
f2.write(str("Vue.use(VueEventCalendar.default, {locale: \'en\', color: \'#4fc08d\'}) //hack here (.default) \
new Vue({ \
  el: \'#example\', \
  data: function () { \
    return { \
      demoEvents:\
	  ["))
#loop through and write to file 
for infile in sorted(glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\graph\\20*.png')):
    
    f2.write(str("{" ))
    
    f2.write(str(("date:" + "\'" + (infile[69:73])+ "/" + (infile[73:75]) + "/" + (infile[75:77]) + "\'")))
    f2.write(str(("title: \'Macquarie Uni\'" )))
    f2.write(str(("desc:<img src=" + "\'" + infile + "\'" )))
    f2.write(str("}," ))



# In[44]:

#Write my block


f2.write(str(("date: \'1996/12/12\'")))
f2.write(str(("title: \'A legend was born\'")))
f2.write(str(("desc: \'Well done for finding my easter egg!\'")))
f2.write(str("}" ))
#Write footer last 4 lines

f2.close()


# In[ ]:



