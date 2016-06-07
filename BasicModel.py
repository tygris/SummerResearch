#Basic Model 
#6/07/2016, Natalie Wellen
#This code is based off of the Basic Model in the May 2016 paper by Gandy and Veraart
#This program only creates the prior distribution of the hierarchical model
# and does not make use of any MCMC or Bayesian Statistics

'''To use this script you will need to define:
		n, the size of the network (number of banks)
		a, the vector of assets for each bank
		l, the vector of liabilities for each bank '''

'''Functions included in this code are:
	function pSame, returns the probability matrix with all off diagoals equal to p
	function adjacency, takes the probabilities in a matrix and randomly asigns edges based on it
	function lamSame, creates a matrix with the same lamda value everywhere
	function bmPrior, creates the prior distribution for our liabilities matrix (a first guess) '''

import random
import numpy as np

'''Definition of constants'''
n = 5              #number of banks/nodes
a = np.ones((1,n)) #each bank's assets
l = np.ones((1,n)) #each bank's liabilities
print 'The number of banks in our network is', n, '.'
print 'The assets of each bank are', a, 
print 'The liabilities for each bank are', l


def psame(n):
	'''Function pSame, returns the probability matrix with all off diagoals equal to p (randomly chosen)
		input: n, the dimensions of the matrix (square matrix)
		output: P, the matrix of probability values for edge ij'''
	#randomly choose pij value (not less than 0.2)
	p = 0
	while(p<0.2):
		p = random.random()
	#Use this to fill in the Probability Matrix P
	P = np.ones((n,n))
	P.fill(p)
	for i in range(0,n):
		P[i,i] = 0
	return P

#Create the Adjacency matrix 
def adjacency(P):
	'''Function adjacency, randomly asigns edges based on a probabilities matrix
		input P, the matrix of probabilities that an edge will be created between each pair of nodes
		output A, the adjacency matrix of our network'''
	n = len(P)
	A=np.zeros((n,n))
	#Fill in edges for the upper triangle
	for j in range (0, n-1):
		for i in range (j+1, n):
			u=random.random()
			if(u<P[i,j]):
				A[i,j] = 1.
	#Fill in edges for the lower triangle
	for i in range (0, n-1):
		for j in range (i+1, n):
			u=random.random()
			if(u<P[i,j]):
				A[i,j] = 1.
	return A
			
def lamSame(n, p, l)
	'''Function lamSame, creates a matrix with the same lamda value everywhere
		input n, the number of nodes in the network
		input p, the probability of an edge between nodes (P[i,j])
		input l, the liability or asset vector
		output Lambda, the matrix of lambdas, the paramater for weight distribution(~Exp)'''
	#choose lambda
	A = np.sum(l)
	lam = (p*n*(n-1))/A #formula from Gandy & Veraart May 2016 Section 5.3.1
	#create the matrix
	Lambda = np.ones((n,n))
	Lambda = Lambda.fill(lam)
	return Lambda

def bmPrior(A, Lambda)
	'''Function bmPrior, creates the prior distribution for our liabilities matrix (a first guess)
		input A, the adjacency matrix that marks which edges we need to weight
		input Lambda, contains the parameter to weight the edges (~Exp)
		output L, an admissable Liabilities Matrix '''
	L = A		#assign L to fill in
	n = len(L)	#the number of banks in the network
	for i in range(0,n):
		for j in range(0,n):
			if(L[i,j] == 1.):
				L[i,j] = np.random.exponential(Lambda[i,j])
	return L
			
#we have A
print 'A = ', A
print 'm = ', m

print 'The lambda we chose is:', lam

#We have completed our Liabiities matrix!
print "The liabilities matrix is " 
print L

