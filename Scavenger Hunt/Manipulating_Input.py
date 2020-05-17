########################################################################################
# Name: Raven A. Alexander
# Date: March 30, 2020
# Description: This program recieves a binary string from stdin and displays its ASCII
# equivalent.
########################################################################################
import sys

##function that converts binary to ASCII
def bin_to_ASCII(a,b,n):
    count = 0
    #seperates the the binary string into sets of 7 or 8 characters
    for i in a:
        b += i
        count += 1
        #converts binary set into ASCII
        if (count == n):
            b = int(b,2)
            sys.stdout.write(str(chr(b)))
            b = ''
            count = 0
            if(n == 8):
                n = n-1
            else:
                n = n+1
    print
        
######################################## MAIN ##########################################
tmp_bin = ''
#reads stdin
nums = str(sys.stdin.read())

#checks if 8-bit binary or 7-bit binary
'''if ((len(nums)-1)%7 == 0):
    bit = 7
else:
    bit = 8 '''
#calls function
bin_to_ASCII(nums,tmp_bin,7)

        

    
