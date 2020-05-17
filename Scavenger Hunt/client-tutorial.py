########################################################################################
# Name: Raven A. Alexander
# Date: April 24, 2020
# Description: This program connects to a server, grabs an overt message and decodes
# a covert message using the times between characters in the overt message.
# PYTHON 3.7.7
########################################################################################
import socket
from sys import stdout
from time import time
from binascii import unhexlify

# enables debugging output
DEBUG = False

# set the server's IP address and port
ip = "138.47.99.163"
port = 12321
covert_bin = ""
ONE = .16

# create the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
s.connect((ip, port))

# receive data until EOF
data = s.recv(4096)
while (data.rstrip("\n") != "EOF"):
    # output the data
    stdout.write(data)
    stdout.flush()
    # start the "timer", get more data, and end the "timer"
    t0 = time()
    data = s.recv(4096)
    t1 = time()
    # calculate the time delta (and output if debugging)
    delta = round(t1 - t0, 3)
    if (delta > .19):
        covert_bin += "1"
    elif(delta < .11):
            covert_bin += "0"
    if (DEBUG):
        stdout.write(" {}\n".format(delta))
        stdout.flush()
# close the connection to the server
s.close()
######################################### MAIN #########################################
covert = ""
i = 0
# convert data until EOF
while(i < len(covert_bin)):
    # convert binary to hex
    b = covert_bin[i:i + 8]
    n = int ("0b{}".format(b),2)
    # convert hex to ascii
    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    i += 8
    # stop coversion after EOF
    if(covert[-3:] == "EOF"):
        break
#output data
stdout.write("\nCovert message:{}\n".format(covert))
