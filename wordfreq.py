#!/usr/bin/env python

#File: wordfreq.py
#Purpose: Meant to frequency of words in a file with more than three letters, ordered by frequency

#Below imports necessary functions
import sys
args = sys.argv

#Below opens and reads the file
words = {} #Dictionary to hold words and frequencies
filename = open(args[1], 'r')
rawfile = filename.read()

#Below takes out punctuation in read-in string
openfile = ''
for g in range(0, len(rawfile)):
	if not rawfile[g].isalpha() and not rawfile[g].isspace(): #Takes only letters
		continue
	openfile = openfile + rawfile[g]
split = openfile.split() #Splits by white space

#Adds each word and frequency in current line to dictionary
for c in range(0, len(split)):
	#Skips word if contains 3 letters or less
	if len(split[c].lower()) <= 3:
		continue
		
	#Adds word if not yet in dictionary
	if split[c].lower() not in words:
		words[split[c].lower()] = 1
	#Increments frequency if word already in dictionary
	elif split[c].lower() in words:
		words[split[c].lower()] = words[split[c].lower()] + 1
				
#Below sorts dictionary entries
for d in range(0, len(words)):
	currfreq = -1
	currword = None
	
	#Below considers each key in dictionary
	for key in words:
		if currfreq <= words[key]: #More frequent word found
			currword = key
			currfreq = words[key]
	
	#Below 'deletes' current chosen word from consideration
	words[currword] = (-1)*float('inf')
	
	#Below prints most frequent word found
	print(currword + ': ' + str(currfreq))

	
			
	


