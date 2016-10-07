#expoDistribution 
#10/07/2016, Natalie Wellen
import random
import numpy as np
import matplotlib.pyplot as plt

#This file contains functions that can be used to sample exposures between banks or plot histograms 
#of these values. 


'''exposureFrac is a function that calculates the fraction used to estimate exposures in Duffie and Zhu
	input m, the illiquidity measure of the asset class
	input Z, the vector of gross notional values for the banks in the network
	output n, the umber of banks in the network
	output frac, the value used to estimate 
	'''
def exposureFrac(Z, m):
	n = Z.size #n is the number of banks in the system
	frac = np.ones((n,n))
	for i in range(0,n):
		for j in range(0,n):
			if(i != j):
				frac[i,j] = m*Z[i]*Z[j]/(np.sum(Z[0:i])+np.sum(Z[(i+1):n]))
			else:
				frac[i,j] = 0
	return n, frac 
	
'''duffie, a function that uses the notionals as the standard deviation of a normal r.v. with mean 0
	This is the model that Duffie and Zhu propose for any given asset class
	input n, the number of banks in the network 
	input eFrac, the matrix of values used to estimate exposure from bank i to j
	output exposure, the matrix of exposure values for each bank
	'''
def duffie(n, eFrac, normal):
	exposure = np.ones((n,n))
	for i in range (0,n):
		for j in range (0,n):
			if(i != j):
				exposure[i,j] = np.random.normal(0, eFrac[i,j])
			else:
				exposure[i,j] = 0
	return exposure

'''cont, a function that uses notionals as a constant multiplied by a probability distribution 
	this is the model proposed by Cont and Kokholm 
	input n, the number of banks in the network 
	input eFrac, the matrix of values used to estimate exposure
	input normal, if true then use a standard normal distibution, if false use a t distribution	
		with degree of freedom 3
	output exposure, the estimated exposure from bank i to j
	'''	
def cont(n, eFrac, normal):
	exposure = np.ones((n,n))
	if(normal):
		for i in range (0,n):
			for j in range (0,n):
				if(i != j):
					exposure[i,j] = np.random.normal(0, 1)*eFrac[i,j]
				else:
					exposure[i,j] = 0
	if not normal:
		for i in range (0,n):
			for j in range (0,n):
				if(i != j):
					exposure[i,j] = np.random.standard_t(3)*eFrac[i,j]
				else:
					exposure[i,j] = 0
	return exposure
	

'''sampleChain, creates a list of randomly sampled values that can later be plotted in a histogram
input l, the legth of the list to be created
input fun, the function we are running to create the list with
input normal, a true false value that states if we use the normal distribution (true) or t-distribution.
input Z, the gross notional data on the banks in the network
input beta, the the illiquidity measure of the asset class
output chain, a list lists of randomly sampled values from the function fun, entry [ij] is n*i+j in list
'''
def sampleChain(l, fun, normal, Z, beta):
	#find the number of banks and exposure vector
	n, exposures = exposureFrac(Z, beta)
	#create a list to save data in
	chain = []
	#create the samples and append to chain
	for i in range (0, l):
		s = fun(n, exposures, normal)
		chain.append(s)
	return chain
	
	
'''listafy, takes a list of matrices and organizes each entry in the matrix list into a list of its own
input chain, the chain of matrices
input l, the length of the chain
output entry, the lis of lists for each entry, entry i,j is at l*i+j in list
'''
def listafy(chain, l):
	#list of lists
	entry = []
	m = chain[1]
	#number of banks in the system
	n = len(m)
	for i in range (0, n):
		for j in range (0,n):
			list = []
			for k in range (0, l):
				matrix = chain[k]
				item = matrix[i,j]
				list.append(item)
			entry.append(list)
	return entry

'''histCompare, this function compares the exposure distributions entry by entry for the network
input z, the gross notional data for the system
input m, the illiquidity measure of the market
input l, the number of samples to plot on the histogram
input dist1, the function that samples the exposures for a bank network
input dist2, the comparison function to dist1
input normal, True if use normal distribution, False for t-distribution
output, non, though this function will plot histograms for each non-diagonal entry 
'''
def histCompare(z, m, l, dist1, dist2, normal):
	chain1 = sampleChain(l, dist1, normal, z, m)
	chain2 = sampleChain(l, dist2, normal, z, m)
	histogram1 = listafy(chain1, l)
	histogram2 = listafy(chain2, l)
	#want indices of histogram that are for non-diagonal entries
	n = len(z)
	vals = np.arange(n)+1
	for i in range(1,n):
		vals = np.append(vals, np.arange(n)+n*i+i+1, axis=0)
	#plot the data
	for i in vals[0:n**2-n]:
		plt.figure()
		plt.hist((histogram1[i], histogram2[i]), label = [dist1.func_name, dist2.func_name])
		name = "Exposures from bank " + str(int(i/n)+1) +" to bank " + str(i-int(i/n)*n+1)
		plt.title(name)
		plt.xlabel("Exposure")
		plt.ylabel("Frequency")
		plt.legend()
		plt.show()

