import glob
import argparse
import os

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'integers', metavar='int', type=int, choices=range(10),
        nargs='+', help='an integer in the range 0..9')
    parser.add_argument(
        '--sum', dest='accumulate', action='store_const', const=sum,
        default=max, help='sum the integers (default: find the max)')

    args = parser.parse_args()
    print(args.accumulate(args.integers))

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
    currentFile = os.path.basename(infile)

    f2.write(str("{"))
    f2.write(str(("date:" + "\'" + (currentFile[0:3]) + "/" + (currentFile[4:5]) + "/" + (currentFile[6:7]) + "\'")))
    f2.write(str(("title: \'Macquarie Uni\'")))
    f2.write(str(("desc:<img src=" + "\'" + infile + "\'")))
    f2.write(str("},"))

#Write my block

f2.write(str("{"))
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