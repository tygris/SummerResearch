#Basic Model 
#6/03/2016, Natalie Wellen

import random
import numpy as np

#n is the number of banks in the network
n = 5
#We assume we know each bank's assets and liabilities,which are given here
a = np.ones((1,n)) #each bank's assets
l = np.ones((1,n))#each bank's liabilities
print 'The assets of each bank are:', a
print 'The liabilities for each bank are:', l
#To keep track of the values we know in each row and column
a_known = np.ones((1,n)) #we know all of the diagonal entries
a_sum = np.zeros((1, n)) #all of our know entries add to zero
l_known = np.ones((1, n))
l_sum = np.zeros((1,n))

#This model assumes p_ij and lamda_ij are the same for all i,j
#randomly choose pij value (not less than 0.2)
p = 0
while(p<0.2):
	p = random.random()
print('P_ij = '); print(p)

#Create the Adjacency matrix 
A=np.zeros((n,n))
#while doing so keep track of fixed values (0 in A)
m=0 #our counting variable
#Fill in edges for the upper triangle
for j in range (0, n-1):
	for i in range (j+1, n):
		u=random.random()
		if(u<p):
			A[i,j] = 1
		else:
			m=m+1
#Fill in edges for the lower triangle
for i in range (0, n-1):
	for j in range (i+1, n):
		u=random.random()
		if(u<p):
			A[i,j] = 1
		else:
			m=m+1
#we have A
print('A = '); print(A)
print('m = '); print(m)

#calculate degree of freedom (here is where we need to know m)
#if zero simply fill in missing values
#if not, skip nothing! 
dof = n*n - 3*n + 1 - m
if(dof<0):
	dof=0
print('The Degree of Freedom in our network is:'); print(dof)

if(dof>0):
#choose lambda
	TL = np.sum(l)
	lam = (p*n*(n-1))/TL
#weight the adjacency matrix with lamda

#define the asset(a) and liabilities(l) vectors

#define the row and column sum 

#fill in known values of matrix
#Will need some way of keeping track for when something is unknown, and if only one then we can fill it in!
#function that takes total(a_j or l_i) and subtract known values from them 

#sample and fill in the liabilities matrix degrees of freedom

#fill in the known values of the matrix