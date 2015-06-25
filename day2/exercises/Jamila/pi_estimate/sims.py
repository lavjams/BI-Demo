######
###BACKGROUND
#Below Section: Imports necessary functions
import numpy as np
import matplotlib.pyplot as graph
import random as rand
import time as watch
pi = np.pi

######
###SIMULATIONS

#FUNCTION: ishit
#PURPOSE: This function is meant to test whether or not a given 2d point is within the unit circle.
#INPUTS: x = x-axis location, y = y-axis location
#OUTPUT: Boolean
def ishit(x, y):
	#Below Section: Calculates (x, y) vector distance from origin using Pythagorean theorem
	hyplength = np.sqrt(x**2 + y**2)
	
	#Below Section: Returns whether or not length within unit circle or not
	if hyplength <= 1:
		return True
	else:
		return False
	
	

#FUNCTION: simdarts
#PURPOSE: This function is meant to simulate a dart game, with the goal of hitting the inner circle.
#INPUTS: Number of times to 'throw' a dart
#OUTPUTS: Arrays of x and y locations where the dart falls each time; estimated pi value
def simdarts(num):
	#Below Section: Simulates given number of dart throws
	num = int(num)
	xlocs = np.zeros(num) #X-axis locations
	ylocs = np.zeros(num) #Y-axis locations
	
	#Below generates the random numbers in [0, 1)
	for a in range(0, num):
		xlocs[a] = rand.random()
		ylocs[a] = rand.random()
		
	#Below Section: Estimates the value of pi using the results
	count = 0
	for b in range(0, num):
		if ishit(x=xlocs[b], y=ylocs[b]):
			count = count + 1
		
	#Below Section: Returns the calculated values
	#NOTE: Multiplies proportion by four to account for percentage of total circular area
	return {'xs':xlocs, 'ys':ylocs, 'estpi':(count/1.0/num)*4}
	
	
