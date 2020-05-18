from sys import stdin, stdout 

nFile = "notbin.txt"
nFile = open(nFile,"r")
nString = nFile.read()

for char in nString:
	if char == "0" or char == "1":
		stdout.write(char)

