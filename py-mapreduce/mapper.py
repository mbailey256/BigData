#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()
	# split the line into words
	words = line.split()
	# increase couters
	for word in words:
		#write the results to STDOUT (standar output);
		#wht we output here will be the input for the 
		#Reduce step, i.e. the input for the reducer.py
		#
		# tab-delimited; the trivial word count is 1
		print '%s\t%s' % (word, 1)

