###############################
# Written in Python 3
###############################

from sys import stdout, argv

#create the sentinel bytearray
SentinelBytes = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
Sentinel = bytearray(SentinelBytes)

#------------Storage / Extraction functions-------------#

#the storage functions more or less follow the pseudocode given
def Storage_Byte(offset,  interval, wrapper, hidden):
    W = wrapper
    H = hidden
    
    i = 0
    while(i < len(H)):
        W[offset] = H[i]
        offset += interval
        i += 1

    i = 0
    while(i < len(Sentinel)):
        W[offset] = Sentinel[i]
        offset += interval
        i += 1

    return bytearray(W)

def Storage_Bit(offset, interval, wrapper, hidden):
    W = wrapper
    H = hidden

    i = 0
    while(i < len(H)):
        
        for j in range(0,8):
            W[offset] &= 11111110
            W[offset] |= ((H[i] & 10000000) >> 7)
            H[i] = (H[i] << 1) & (2 ** 8 - 1)
            offset += interval

        i += 1
    
    i = 0
    while(i < len(Sentinel)):
        for j in range(0, 8):
            W[offset] &= 11111110
            W[offset] |= ((Sentinel[i] & 10000000) >> 7)
            Sentinel[i] = (Sentinel[i] << 1) & (2 ** 8 - 1)
            offset += interval
        
        i += 1

    return bytearray(W)

#the extraction functions follow the pseudocode given, but
#both contain a unique solution to identifying the Sentinel
def Extraction_Byte(offset, interval, wrapper):
    W = wrapper
    H = []
    tempByteArray = []

    while(offset < len(W)):
        b = W[offset]
        
        #check to see if b is equal to the first byte of the sentinel
        if(b == Sentinel[0]):

            #create a temp offset variable to traverse the
            #wrapper array temporarily to check for the sentinel
            tempOff = offset

            #append 6 bytes from the wrapper to the temporary
            #array and then check it
            for byte in Sentinel:
                tempByteArray.append(W[tempOff])
                tempOff += interval
            
            #if you've hit the sentinel, go ahead and return
            #the hidden file--
            #else, clear the temp array and proceed like nothing happened
            if(bytearray(tempByteArray) == Sentinel):
                return bytearray(H)
            else:
                tempByteArray = []

        H.append(b)
        offset += interval

def Extraction_Bit(offset, interval, wrapper):
    W = wrapper
    H = []
    off = offset
    inter = interval
    tempByteArray = []

    #create a "hit counter" to see if the bytes going to be added are
    #the sentinel -- with enough hits, the hidden file will be returned
    hitCounter = 0

    while(off < len(W)):
        b = 0
        
        for j in range(0,8):
            b |= (W[offset] & 0b00000001)
            if(j < 7):
                b = (b << 1) & (2 ** 8 - 1)
                offset += interval
        
        #if b is a sentinel byte, check then to see if it is in
        #the same order as the sentinel's
        if(b in Sentinel):

            #if it is in the right order, append it and increment
            #the hit counter
            if(b == Sentinel[hitCounter]):
                tempByteArray.append(b)
                hitCounter += 1
            #if not the right order, add everything from the temp array
            #to the hidden file, clear the temp, reset the hit counter
            #then move on
            else:
                if(len(tempByteArray) > 0):
                    for byte in tempByteArray:
                        H.append(byte)
                H.append(b)
                hitCounter = 0
                tempByteArray = []
            
            #if 6 correct bytes in a row, return the hidden file
            if(hitCounter == 5):
                return bytearray(H)
        
        #similar to what happens when the byte is in sentinel but not 
        #in the correct order
        else:
            if(len(tempByteArray) > 0):
                for byte in tempByteArray:
                    H.append(byte)
            H.append(b)
            hitCounter = 0
            tempByteArray = []

        offset += interval


#----------------MAIN-----------------#

#put everything in a try/catch block to ensure everything is needed to run;
#if an index error occurs due to not having enough arguments, return usage
#if a file is not found, return a message saying one was not found
try:  
    Action = argv[1]
    
    Method = argv[2]
    
    #must remove the -w and -h from the wrapper and the hidden files
    wrapperFile = argv[5]
    wrapperFile = wrapperFile[2:]

    if(Action == "-r"):
        pass
    else:
        hiddenFile = argv[6]
        hiddenFile = hiddenFile[2:]

    #get interval and offset, and if only -i or -o is given,
    #set each to their default values
    offset = argv[3]
    interval = argv[4]

    if(len(offset) == 2):
        offset = 0
    else:
        offset = int(offset[2:])

    if(len(interval) == 2):
        interval = 1
    else:
        interval = int(interval[2:])

    #open the files--
    #if -r is given at command line, the don't bother to
    #read from a hidden file
    with open(wrapperFile, "r") as File:
        wrapper = bytearray(File.buffer.read())
    
    if(Action == "-r"):
        pass
    else:
        with open(hiddenFile, "r") as File:
            hidden = bytearray(File.buffer.read())
    
    #perform an appropriate action based off of arguments given
    if (Action == "-s" and Method == "-B" ):
        stdout.buffer.write(Storage_Byte(offset, interval, wrapper,hidden))

    elif (Action == "-s" and Method == "-b"):
        stdout.buffer.write(Storage_Bit(offset, interval, wrapper, hidden))

    elif (Action == "-r" and Method == "-B" ):
        stdout.buffer.write(Extraction_Byte(offset, interval,wrapper))
    
    elif (Action == "-r" and Method == "-b"):
        stdout.buffer.write(Extraction_Bit(offset, interval, wrapper))

    #if there's a spelling error somewhere in the command,
    #give a usage
    else:
        print("Usage python3 Steg.py -(sr) -(bB) -o<val> [-i<val>]"+ \
                "-w<val> [-h<val>]")

except FileNotFoundError:
    print("One of the files specified wasn't found!")

except IndexError:
   print("Usage: python3 Steg.py -(sr) -(bB) -o<val> [-i<val>]"+ \
          "-w<val> [-h<val>]")


