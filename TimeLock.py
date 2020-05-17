#USE PYTHON 2

from sys import stdin, argv
from datetime import datetime
from hashlib import md5
import pytz

#just used for setting the current time to a value
DEBUG = False

#used to make a time zone for converting datetimes to UTC
local_time = pytz.timezone("America/Chicago")

#used to convert the time difference into a code
def myCode(time):
    
    code = ""

    #sets the time value to the beginning of a 60 sec interval
    temp = time.total_seconds()
    temp = temp - temp%60

    #various type castings in order to double-MD5 the time value
    temp  = str(int(temp))
    temp = md5(temp)
    temp = temp.hexdigest()
    temp = md5(str(temp))
    temp = temp.hexdigest()

    #different loops for creating the code out of the hash
    i = 0
    while(len(code) < 2 and i < len(temp)):
        if(temp[i] in ["a","b","c", "d", "e", "f"]):
            code += temp[i] 
        i+=1

    i = len(temp)-1
    while(len(code) < 4 and i > 0):
        if(temp[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]):
            code += temp[i]

        i-=1

    return code


if DEBUG:
    current = datetime(2017, 04, 26, 15, 14, 30)

else:
    current = datetime.now()

#used to determine how input is given (trys command-line arguments first,
#then tries reading from stdin
try:
    epoch  = datetime(int(argv[1]), int(argv[2]), int(argv[3]),\
            int(argv[4]),int(argv[5]), int(argv[6]))

except IndexError: 
    epoch = stdin.read().rstrip("\n")
    epoch = datetime.strptime(epoch, "%Y %m %d %H %M %S")


#converts the datetie objects to UTC time
current = local_time.localize(current, is_dst=None)

current = current.astimezone(pytz.utc)

epoch = local_time.localize(epoch, is_dst=None)

epoch = epoch.astimezone(pytz.utc)

#calculate the time difference and then print the corresponding code
t = current - epoch

print myCode(t)
