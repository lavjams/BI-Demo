######
###BACKGROUND
#Below Section: Imports necessary functions
import numpy as np
import matplotlib.pyplot as graph
import random as rand
import time as watch
pi = np.pi


#FUNCTION: ishit
#PURPOSE: This function is meant to test whether or not a given 2d point is within the unit circle.
#INPUTS: x = x-axis location, y = y-axis location
#OUTPUT: Boolean
def ishit(x, y):
	#Below Section: Calculates (x, y) vector distance from origin using Pythagorean theorem
	hyplength = np.sqrt(x**2 + y**2)
	
	#Below Section: Returns whether or not length within unit circle or not
	if hyplength >= 1:
		return True
	else:
		return False
	
	

#FUNCTION: simdarts
#PURPOSE: This function is meant to simulate a dart game, with the goal of hitting the inner circle.
#INPUTS: Number of times to 'throw' a dart
#OUTPUTS: Arrays of x and y locations where the dart falls each time; estimated pi value
def simdarts(num):
	#Below Section: Simulates given number of dart throws
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
	return {'xs':xlocs, 'ys':ylocs, 'estpi':(count/1.0/num)}
	
	

#FUNCTION: histdarts
#PURPOSE: This function is meant to plot a histogram of the estimated pi value of several dart simulations.
#INPUTS: Number of histogram points; number of darts per simulation
def histdarts(numdarts, numsims):
	#Below Section: Generates several simulations of given number of darts each
	estpis = np.zeros(numsims)
	for c in range(0, numsims):
		estpis[c] = simdarts(num=numdarts)['estpi']
		
	#Below Section: Graphs results in histogram
	meanstring = 'Mean: {:.4f}, '.format(np.mean(estpis))
	stdstring = 'St. Dev: {.4f}'.format(np.std(estpis))
	graph.hist(estpis, histtype='step', alpha=.6)
	graph.title('Histogram of Pi Estimations')
	graph.suptitle(meanstring+stdstring)
	graph.xlabel('Estimated Pi Values')
	graph.ylabel('Frequencies')
	#graph.savefig('EstPiHist-'+numdarts'Darts-'+numsims+'Sims')
	graph.show()
	graph.close()
	
	
	
#FUNCTION: drawdarts
#PURPOSE: This function is meant to draw the darts for a given simulation within the unit square.
#INPUTS: X- and Y- locations of the simulated darts
def drawdarts(x, y):
	#Below Section: Scatters the simulated darts
	graph.scatter(x, y, color='blue', alpha=.4)
	
	#Below Section: Plots a circle as a guideline to show boundaries of unit circle
	xcircle = np.linspace(0, 1, 1000)
	ycircle = np.sqrt(1 - xcircle**2)
	graph.plot(xcircle, ycircle, color='cyan', alpha=.2, linestyle='--')
	#graph.savefig('EstPiDraw-'+str(len(x))+'Darts')
	graph.show()
	graph.close()
	
	
	
	
#FUNCTION: plottime
#PURPOSE: This function is meant to plot the dependence of time upon the number of darts.
#INPUTS: An array containing the number of darts for each simulation
def plottime(numdartsarray):
	#Below Section: Times the dart simulation for each number of darts given
	simtimes = np.zeros(len(numdartsarray))
	for d in range(0, len(numdartsarray)):
		starthere = watch.time() #Start time
		simhere = simdarts(num=numdartsarray[d]) #Simulation
		endhere = watch.time() #End time
		
		#Below records time taken for current simulation
		simtimes[d] = endhere - starthere
		
	#Below Section: Plots the time taken
	graph.plot(numdartsarray, simtimes, alpha=.4, color='purple')
	graph.title('Time Dependence of the Number of Darts')
	graph.xlabel('Number of Darts')
	graph.ylabel('Time Dependence')
	graph.show()
	graph.close()
	
	
	
#FUNCTION: plotacc
#PURPOSE: This function is meant to plot the dependence of accuracy upon the number of darts.
#INPUT: An array containing number of darts for each simulation
def plotacc(numdartsarray):
	#Below Section: Determines accuracy for each number of darts given
	simacc = np.zeros(len(numdartsarray))
	for e in range(0, len(numdartsarray)):
		esthere = simdarts(num=numdartsarray[e])['estpi']
		
		#Below calculates and records current accuracy
		simacc[e] = abs(esthere - pi)
		
	#Below Section: Graphs the accuracy of pi estimations
	graph.plot(numdartsarray, simacc, alpha=.4, color='orange')
	graph.title('Estimation Accuracy of the Number of Darts')
	graph.xlabel('Number of Darts')
	graph.ylabel('Accuracy of Pi Estimation')
	graph.show()
	graph.close()
		
	
	
	

