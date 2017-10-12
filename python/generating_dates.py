
# coding: utf-8

# In[50]:

# Python version
import sys
# In addition to the online example, these packages below help dealinf with the file system
import glob
import os


# In[3]:

dir = '../data/*'
names = ['UTCDateTime', 'LocalDateTime', 'Temperature', 'Counts', 'Frequency', 'MSAS']
print(glob.glob(dir))


# In[9]:

# Set the common time grid onto which each night is sampled. The common grid
# is defined by the start time defined below, and the number of hours from that time
beginh = 16 # Hour of start time (hour)
beginm = 30 # Hour of start time (minute)
nhrs = 15   # Number of hours to extend time grid

#print  (glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\daily\\20*.dat'))

numbfile = len(glob.glob('../data/20*.dat'))
print (numbfile)


# In[59]:

javascript= '../html/js/darkskiesdata.js'
f2=open(javascript,'w')
#Write Header first 7 lines
f2.write(str("Vue.use(VueEventCalendar.default, {locale: \'en\', color: \'#4fc08d\'}) \n \
new Vue({\n \
  el: \'#example\',\n \
  data: function () { \n\
    return {\n \
      demoEvents:\n\
	  [\n\n"))
#loop through and write to file
for infile in sorted(glob.glob('../demodata/mu_graph/20*.png')):


   currentFile = os.path.basename(infile)


   f2.write(str("{\n" ))
   #print (("date:" + "\'" + (currentFile[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\'"))
   f2.write(str(("date:" + "\'" + (currentFile[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\',\n")))
   f2.write(str(("title: \'Macquarie Uni\',\n" )))
   f2.write(str(("desc: \'" + currentFile +"'\n" )))
   f2.write(str("},\n" ))

#data file download?
#root acess?
#

# In[ ]:
for infile2 in sorted(glob.glob('../demodata/sso_graph/20*.png')):


   currentFile2 = os.path.basename(infile2)


   f2.write(str("{\n" ))
   #print (("date:" + "\'" + (currentFile2[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\'"))
   f2.write(str(("date:" + "\'" + (currentFile2[0:4])+ "/" + (currentFile2[4:6]) + "/" + (currentFile2[6:8])+ "\',\n")))
   f2.write(str(("title: \'Siding Springs\',\n" )))
   f2.write(str(("desc: \'" + currentFile2 +"'\n" )))
   f2.write(str("},\n" ))
#


# In[54]:

#Write my block

f2.write(str("\n{\n" ))
f2.write(str(("date: \'1996/12/12\',")))
f2.write(str(("title: \'A legend was born\',")))
f2.write(str(("desc: \'Well done for finding my easter egg!\'")))
f2.write(str("}\n\n" ))
#Write footer last 4 lines

f2.write(str("            ]\n"))
f2.write(str("        }\n"))
f2.write(str("    }\n"))
f2.write(str("  }\n);\n"))

f2.close()


# In[ ]:
