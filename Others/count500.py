import re
import datetime


#open location of log
f = open("access_log")
lines = f.readlines()

# get datetime now without microseconds
datenow = datetime.datetime.now().replace(microsecond=0)

####
#inputan = '10/Oct/2000:14:56:36'
#datenow = datetime.datetime.strptime(inputan,'%d/%b/%Y:%H:%M:%S');
####

count=0

limitminutes = 10;
#print lines
for line in lines:
   newline = re.sub("^.*?\[(.*?)\s.*$", "\\1",line)
#   newline = re.sub("^\s$","" , newline)
   newdate = newline.strip()
#   print newline
   datelog = datetime.datetime.strptime(newdate,'%d/%b/%Y:%H:%M:%S')
   selisih = datenow - datelog
   selisihint = (selisih).days * 86400 + (selisih).seconds
   selisihfinal = divmod(selisihint,60)[0]


   if selisihfinal <= limitminutes:
       printfilter = bool(re.search("^.*\s500\s.*$",line))
       if printfilter:
           count=count+1
##       count=count+1
           print line,

#   print newline,
# newline = re.sub("^\s*#.*$", "",line) from first ^ , followed by space \s or not (\s*) and #, untill the end of line(followed by others (.*) until last line ($)
print ("Request per %i minute(s) : %i" %(limitminutes,count))
