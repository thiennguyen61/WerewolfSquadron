#IMPORTANT -- made using python 2.7

#ftplib and globals to change
import ftplib

host = "jeangourd.com"
port = "21"
login = "anonymous"
password = ""
target = "10/"
METHOD = 10

#captures the directory listing as an array
myFetch = []

#get in the server, navigate to the dir, get the listing, then dip out
ftp = ftplib.FTP()

ftp.connect(host, port)
ftp.login(login,password)

ftp.cwd(target)
ftp.dir(myFetch.append)

ftp.quit()

#converts the listing into a binary sequence depending on
#the method passed to it (7 or 10)
def FTPConvert(listing, bits):
    
    permissions = ""
    myMessage = ""

    if (bits == 7):
        
        for i in listing:
            if(i[0] == "-" and i[1] == "-" and i[2] == "-"):
                for k in range(3,10):
                    permissions += i[k]
        
        for char in permissions:
            if (char != "-"):
                myMessage += "1"

            else:
                myMessage += "0"
    
    if (bits == 10):

        for i in listing:
            for k in range(0,10):
                permissions += i[k]

        for char in permissions:
            if (char != "-"):
                myMessage += "1"

            else:
                myMessage += "0"
        
        #this last little thing checks to make sure the message
        #is divisible by 10, and if not, fluff it out with extra bits
        if (len(myMessage)%10 != 0):
            while(len(myMessage)%10 != 0):
                myMessage += myMessage + "0"

    return myMessage

#I literally just yanked this function from my binary decoder program,
#with an added check to make sure I ignore any lingering bits
#that are not meant to be apart of any character
def BinaryDecoder(x, bits):
    y = ""
    i = 0

    while( i < len(x)):
    
        if(len(x[i:i+bits]) != 7):
            return y
        else:
            if(int(x[i:i+bits],2) == 8):
                y = y[0:len(y)-1]
                i+=bits

            else:
                y+= chr(int(x[i:i+bits], 2))
                i+=bits

    return y

#then print out the message based off of the method chosen
if (METHOD == 7):
    print BinaryDecoder(FTPConvert(myFetch, METHOD), METHOD)

elif (METHOD == 10):
    print BinaryDecoder(FTPConvert(myFetch, METHOD), 7)



