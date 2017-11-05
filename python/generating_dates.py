import sys
import glob
import os

# This below is just a logic check to make sure that you aren't using an empty directory, so to make sure you have
# your directory right before you try filling the array, i've hashed it out as it is not really needed for the code
# but could be useful when adding a new location or directory

#numbfile = len(glob.glob('../data/20*.dat'))
#print (numbfile)

# Below is where the java script is created, this shouldnt break, and there is no need to edit it, this part is
# completely static

javascript= '../html/js/darkskiesdata.js'
f2=open(javascript,'w')
f2.write(str("var darkSkyEvents; \
darkSkyEvents = \
    ["))

#######################################################################################################################
                                   # DO NOT EDIT ABOVE THIS LINE #
#######################################################################################################################

#The below loops create a java script array containing all the details needed to populate the calander on the websie

#This one bellow is for the Uni observatory
for infile in sorted(glob.glob('../demodata/mu_graph/20*.png')):


   currentFile = os.path.basename(infile)


   f2.write(str("{\n" ))
   #print (("date:" + "\'" + (currentFile[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\'"))
   f2.write(str(("date:" + "\'" + (currentFile[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\',\n")))
   f2.write(str(("title: \'Macquarie Uni\',\n" )))
   f2.write(str(("desc: \'" + currentFile +"'\n" )))
   f2.write(str(("graph: \'" + "images/" + currentFile + "'\n")))
   f2.write(str(("dataFile: \'" + "data/" + (currentFile[0:24]) + "*.dat" "'\n")))
   f2.write(str("},\n" ))

# This one is for SSO
for infile2 in sorted(glob.glob('../demodata/sso_graph/20*.png')):


   currentFile2 = os.path.basename(infile2)


   f2.write(str("{\n" ))
   #print (("date:" + "\'" + (currentFile2[0:4])+ "/" + (currentFile[4:6]) + "/" + (currentFile[6:8])+ "\'"))
   f2.write(str(("date:" + "\'" + (currentFile2[0:4])+ "/" + (currentFile2[4:6]) + "/" + (currentFile2[6:8])+ "\',\n")))
   f2.write(str(("title: \'Siding Springs\',\n" )))
   f2.write(str(("desc: \'" + currentFile2 +"'\n" )))
   f2.write(str(("graph: \'" + "images/"+ currentFile2 + "'\n")))
   f2.write(str(("dataFile: \'" + "data/" + (currentFile2[0:24]) + "*.dat" "'\n")))#
   f2.write(str("},\n" ))

# Template below
   # If you ever need to add any more locations all you need to do is follow this template, you will need to chang the
   # path in the glob bellow to the location of the new images, which will likely only mean changing the sso_graph to the
   # new folder being used

   # IMPORTANT: the indents must be kept as they are so only remove the hashes, otherwise the loop will not work

#for infile2 in sorted(glob.glob('../demodata/sso_graph/20*.png')):


#  currentFile2 = os.path.basename(infile2)

#  f2.write(str("{\n" ))
#  f2.write(str(("date:" + "\'" + (currentFile2[0:4])+ "/" + (currentFile2[4:6]) + "/" + (currentFile2[6:8])+ "\',\n")))
#  f2.write(str(("title: \'Insert Name of new location\',\n" )))  #This is the line you edit, keep the rest the same
#  f2.write(str(("desc: \'" + currentFile2 +"'\n" )))
#  f2.write(str("},\n" ))


#######################################################################################################################
                                   # DO NOT EDIT BELOW THIS LINE #
#######################################################################################################################


#The below block of code closes the array and once again as before is completely static so need not be messed with

f2.write(str("\n{\n" ))
f2.write(str(("date: \'1996/12/12\',")))
f2.write(str(("title: \'A legend was born\',")))
f2.write(str(("desc: \'Well done for finding my easter egg!\'")))
f2.write(str("}\n\n" ))

f2.write(str("            ];\n"))

f2.close()
