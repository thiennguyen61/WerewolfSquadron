########################################################################################
# Name: Raven A. Alexander
# Date: April 3, 2020
# Description: This program opens an ftp server, grabs data from a folder and decodes
# the data using a binary decoder.
# PYTHON VERSION: 3.7.7
########################################################################################
#LIBRARIES
from ftplib import FTP
import sys

#NONVOLATILE VARIABLES
IP ="138.47.99.163"
PORT = 21
ftp = FTP()
METHOD = 10
#METHOD = 10
FOLDER = "FILES"
#FOLDER = "10bit"
USER = "valkyrie"
PASS = "readytoride"

#VOLATILE VARIABLES
contents = []

#connects to ftp server, grabs data and disconnects
def ftp_connect(contents,IP,PORT,FOLDER):
    ftp.connect(IP,PORT)
    ftp.login(USER,PASS)
    ftp.cwd(FOLDER)
    ftp.dir(contents.append)
    ftp.quit()
#converts permissions to binary strings
def perm_to_bin(contents,METHOD):
    x = 0
    for data in contents:
        if METHOD == 10:
            data = list(data[:10])
        else:
            data = list(data[3:10])
        y = 0
        for letter in data:
            if (letter == '-'):
                data[y] = '0'
            else:
                data[y] = '1'
            y += 1
        contents[x] = "".join(data)
        x += 1
#decodes binary strings
def decoder(contents):
    for i in contents:
        if len(i) < 7:
            break
        i = int(i,2)
        sys.stdout.write(chr(i))
        
############################################ MAIN ######################################
ftp_connect(contents,IP,PORT,FOLDER)
perm_to_bin(contents,METHOD)
if METHOD == 10:
    contents = "".join(contents)
    contents = [(contents[i:i+7]) for i in range(0,len(contents),7)]
decoder(contents)
print


    
    
