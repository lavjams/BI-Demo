#!/usr/bin/env python

#Imports necessary functions
import sys

#Function: Adds digits of a given number
def sum_digits(x):
	string = str(x)
	sumhere = 0
	for a in range(0, len(string)):
		sumhere = sumhere + int(string[a])
		
	return sumhere


#Script for adding integer multiples of given numbers
args = sys.argv
arg1 = int(args[1])
arg2 = None

#For one-argument case
if len(args) <= 2:
	arg2 = arg1*arg1
elif len(args) > 2:
	arg2 = int(args[2])
	
#Below loops through multiples of first given number
for b in range(1, (arg2/arg1)+1):
	numhere = arg1*b
	print sum_digits(numhere)
	