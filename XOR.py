###################################
# IMPORTANT: written using Python3
###################################

from sys import stdin, stdout

key_file = "key"

#create a bytearray from stdin
my_arr = bytearray(stdin.buffer.read())

#get the key file and make a bytearray out of it
with open(key_file, "r") as f:
    key = bytearray(f.buffer.read())

#create an empty bytearray
message = bytearray()

#xor each byte in the arrays and append it to the message array
i = 0
j = 0
while(i < len(my_arr)):
    message.append(key[j] ^ my_arr[i])
    i+=1
    if(i == len(key)):
        j=0
    else:
        j+=1

#write the bytearray to stdout
stdout.buffer.write(message)

