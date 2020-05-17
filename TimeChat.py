###############################################################
# VERY IMPORTANT: uses a range instead of 2 single variables
# to determine 1s and 0s in message delays (cuz WINDOWS)
#
# ALSO VERY IMPORTANT: made in python 2
###############################################################

import socket
from sys import stdout
from time import time
from binascii import unhexlify

#set port number and host
ip = "localhost"
port = 1337

#variables for one and zero
ONE = .1
ZERO = .025

#used for ranges (cuz Windows IS a little unreliable with the timings)
ONE_MAX = ONE + .005
ONE_MIN = ONE - .005
ZERO_MAX = ZERO +.005
ZERO_MIN = ZERO -.005

covert = ""
covert_bin = ""

# enables debugging output
DEBUG = False

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
        
        #create ranges for the delta to be in
        #since time() in windows is a little random sometimes
        if (delta >= ZERO_MIN and delta <= ZERO_MAX):
            covert_bin += "0"
        elif (delta >= ONE_MIN and delta <= ONE_MAX):
            covert_bin += "1"
        
	if (DEBUG):
		stdout.write(" {}\n".format(delta))
		stdout.flush()

#convert the binary covert message into an ASCII message
i=0
while (i < len(covert_bin)):

    b = covert_bin[i:i+8]
    n = int("0b{}".format(b),2)

    try:
        covert += unhexlify("{0:x}".format(n))
    except TypeError:
        covert += "?"
    
    #stop creating the ASCII message before any random garbage
    #is added after the EOF
    if(covert[len(covert)-3:len(covert)] == "EOF"):
        break
    i += 8


# close the connection to the server
s.close()

#print the covert message without the "EOF" at the end
print "Covert Message: " + covert[:len(covert)-3]
