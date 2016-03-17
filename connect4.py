#!/usr/bin/python
# demo.py - CMD Args Demo By nixCraft
import sys
import exceptions 

# Get the total number of args passed to the demo.py
total = len(sys.argv)
try:
	if total != 4:
		raise InvalidArgumentsException(total)
except(InvalidArgumentsException):
	sys.exit(0)
		
	 
# Get the arguments list 
cmdargs = str(sys.argv)
 
# Print it
print ("The total numbers of args passed to the script: %d " % total)
print ("Args list: %s " % cmdargs)
