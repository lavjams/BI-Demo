######
###BACKGROUND
#Below Section: Imports necessary functions
import numpy as np
import matplotlib.pyplot as graph
import random as rand
import time as watch
import sims
pi = np.pi

######
###PLOTS

#FUNCTION: drawdarts
#PURPOSE: This function is meant to draw the darts for a given simulation within the unit square.
#INPUTS: X- and Y- locations of the simulated darts
def drawdarts(x, y):
	#Below Section: Scatters the simulated darts
	graph.scatter(x, y, color='blue', alpha=.4)
	
	#Below Section: Plots a circle as a guideline to show boundaries of unit circle
	xcircle = np.linspace(0, 1, 1000)
	ycircle = np.sqrt(1 - xcircle**2)
	graph.plot(xcircle, ycircle, color='purple', alpha=.6, linestyle='--', linewidth=3)
	graph.title('Visual Dart Simulation: '+str(len(x))+' Darts')
	graph.xlabel('(Darts Depicted in Blue, Target Outline in Purple)')
	graph.xlim([0,1])
	graph.ylim([0,1])
	#graph.savefig('EstPiDraw-'+str(len(x))+'Darts')
	graph.show()
	graph.close()
	
	
	

#FUNCTION: histdarts
#PURPOSE: This function is meant to plot a histogram of the estimated pi value of several dart simulations.
#INPUTS: Number of histogram points; number of darts per simulation
def histdarts(numdarts, numsims):
	#Below Section: Generates several simulations of given number of darts each
	estpis = np.zeros(numsims)
	for c in range(0, numsims):
		estpis[c] = sims.simdarts(num=numdarts)['estpi']
		
	#Below Section: Graphs results in histogram
	meanstring = 'Mean: {:.4f}, '.format(np.mean(estpis))
	stdstring = 'St. Dev: {:.4f}'.format(np.std(estpis))
	graph.hist(estpis, histtype='step', alpha=.6, bins=50)
	graph.title('Histogram of Pi Estimations: '+str(numdarts)+' Darts Each')
	graph.suptitle(meanstring+stdstring)
	graph.xlabel('Estimated Pi Values')
	graph.ylabel('Frequencies')
	#graph.savefig('EstPiHist-'+numdarts'Darts-'+numsims+'Sims')
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
		simhere = sims.simdarts(num=numdartsarray[d]) #Simulation
		endhere = watch.time() #End time
		
		#Below records time taken for current simulation
		simtimes[d] = endhere - starthere
		
	#Below Section: Plots the time taken
	graph.plot(numdartsarray, simtimes, alpha=.8, color='purple', linewidth=3)
	graph.title('Time Dependence of the Number of Darts (s)')
	graph.xlabel('Number of Darts')
	graph.ylabel('Time Taken by Simulation (s)')
	graph.show()
	graph.close()
	
	
	
#FUNCTION: plotacc
#PURPOSE: This function is meant to plot the dependence of accuracy upon the number of darts.
#INPUT: An array containing number of darts for each simulation
def plotacc(numdartsarray):
	#Below Section: Determines accuracy for each number of darts given
	simacc = np.zeros(len(numdartsarray))
	for e in range(0, len(numdartsarray)):
		esthere = sims.simdarts(num=numdartsarray[e])['estpi']
		
		#Below calculates and records current accuracy
		simacc[e] = abs(esthere - pi)
		
	#Below Section: Graphs the accuracy of pi estimations
	graph.plot(numdartsarray, np.log10(simacc), alpha=.8, color='orange', linewidth=3)
	graph.title('Log10(Estimation Accuracy) by the Number of Darts')
	graph.xlabel('Number of Darts')
	graph.ylabel('Log10(Distance of Pi Estimation from Actual Value)')
	graph.show()
	graph.close()
		
	
	
	
