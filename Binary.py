from sys import stdin

#grab input binary text
input = stdin.read().rstrip("\n");

#make a function that takes a text input and the amount of bits per char
def decoder(x, bits):
    y = ""
    i = 0
    
    while( i < len(x)):
    
        #if the char is a backspace, the remove the last char
        if(int(x[i:i+bits],2) == 8):
            y = y[0:len(y)-1]
            i+=bits
          
        #else add the char ver of the binary collection
        else:
            y += chr(int(x[i:i+bits],2))
            i+=bits
        
    return y

#call the function for each case of 7, 8, or unsure amount of bits
if (len(input)%7 == 0):
    print decoder(input, 7)

elif (len(input)%8 == 0):
    print decoder(input, 8)
    
else:
    print decoder(input, 7)
    print decoder(input, 8)
    
