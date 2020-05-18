#!/bin/bash

# Global variables
MIN_OFFSET=1
MAX_OFFSET=8192
MIN_INTERVAL=1
MAX_INTERVAL=128

# If the args 1 is null or args is null, printout propper format
if [ -z "$1" ] || [ -z "$2" ]; then
	echo "Usage $0 (bB) <wrapper_file>"
	exit
fi
# Parsing the the bite or byte mode
if [ "$1" != "b" ] && [ "$1" != "B" ]; then
	echo "Usage $0 (bB) <wrapper_file>"
	exit
fi
# if args 2 is not file (doesn't exist), error msg and exit
if [ ! -f "$2" ]; then
	echo "$2 doesn't exist!"
	exit
fi

# setting the variables accordingly
method=$1
wrapper="$2"

# Sets offset and loops until max offset, increment in powers of 2. 
# Changed when I needed powers of 2 + 1. "offset=(offset*2)+1"
# Also increments intervals until max interval, for each offset
# Calls my steg.py program with the arguments, and prints the output file with a convenient name "method-offset-interval"
# Deletes file when error occurs (file exist and has a size zero)
for ((offset=MIN_OFFSET; offset<=MAX_OFFSET; offset *=2)); do
	for ((interval=MIN_INTERVAL; interval<=MAX_INTERVAL; interval*=2)); do
		python steg.py -r -$method -o$offset -i$interval -w$wrapper > $method-$offset-$interval
		if [ ! -s "$method-$offset-$interval" ]; then
			rm "$method-$offset-$interval"
		fi
	done
done
