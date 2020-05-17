from sys import argv

#two functions, encrypt and decrypt, depending on the mode
#--makes extensive use of the ord() and chr() functions
#--subtract 65 from each ord() to align each char with range [0-25]
def encrypt(text, key):
    
    plaintext = ""
    
    pos = 0
    
    for char in input:
        
        #check to see if the character ISN'T a letter
        if (ord(char) > 122 or ord(char) < 65):
            plaintext += char
        
        else:
            
            #control flow checks to ensure that only the ciphertext's 
            #capitalization affects the plaintext
                
            if (pos >= len(key)):
                pos = 0

            if (char == char.lower()):
                plaintext += chr((ord(char.upper())-65 +\
                ord(key[pos])-65)%26 + 65).lower()
            
            else:
                plaintext += chr((ord(char)-65 + ord(key[pos])-65)%26 + 65)
         
            pos += 1


            
    return plaintext

def decrypt(text,key):
    plaintext = ""
    
    pos = 0
    
    for char in input:
        
        #check to see if the character ISN'T a letter
        if (ord(char) > 122 or ord(char) < 65):
            plaintext += char
        
        else:
            if (pos >= len(key)):
                pos = 0
            
            #control flow checks to ensure that only the ciphertext's 
            #capitalization affects the plaintext
            if (char == char.lower()):
                plaintext += chr((26 + ord(char.upper())-65\
                - ord(key[pos])-65)%26 + 65).lower()
            
            else:
                plaintext += chr((26 + ord(char)-65\
                - ord(key[pos])-65)%26 + 65)
            
            pos += 1
            
    return plaintext
 
#get the key and mode using the argv[] inputs
key = argv[2].upper()
mode = argv[1]

newKey = ""
for char in key:
    if(not (char == " ")):
        newKey += char

while(1):

    #until there is an EOFerror (ctrl + z then return in windows for me,
    #ctrl + d for linux [that goes for YOU, Dr. Gourd!]),
    #take raw_input and handle it
    try:
        input = raw_input()
        
        if (mode == "-e"):        
            print encrypt(input, newKey)

        elif (mode == "-d"):        
            print decrypt(input, newKey)
    
    except EOFError:
        break

    



        
        
        
        
        
        