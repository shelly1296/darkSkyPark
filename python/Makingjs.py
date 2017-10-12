import glob

javascript = r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\graph\\darkskiesdata.js'
f2 = open(javascript, 'w')
# Write Header first 7 lines
f2.write(str("Vue.use(VueEventCalendar.default, {locale: \'en\', color: \'#4fc08d\'}) //hack here (.default) \
new Vue({ \
  el: \'#example\', \
  data: function () { \
    return { \
      demoEvents:\
	  ["))
# loop through and write to file
for infile in sorted(glob.glob(r'C:\\Users\\Adam Shelbourne\\Uni\\Physics\\Astr310\\Python\\mu\\graph\\20*.png')):
    f2.write(str("{"))

    f2.write(str(("date:" + "\'" + (infile[69:73]) + "/" + (infile[73:75]) + "/" + (infile[75:77]) + "\'")))
    f2.write(str(("title: \'Macquarie Uni\'")))
    f2.write(str(("desc:<img src=" + "\'" + infile + "\'")))
    f2.write(str("},"))

#Write my block


f2.write(str(("date: \'1996/12/12\'")))
f2.write(str(("title: \'A legend was born\'")))
f2.write(str(("desc: \'Well done for finding my easter egg!\'")))
f2.write(str("}" ))
#Write footer last 4 lines

f2.write(str("]"))
f2.write(str("}"))
f2.write(str("}"))
f2.write(str("}}"))

f2.close()