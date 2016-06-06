#Basic Model 
#6/04/2016, Natalie Wellen
#This model is only the prior distribution of the hierarchical model
# and does not make use of any MCMC or Bayesian Statistics

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


#function that takes total(a_j or l_i) and subtract known values from them 
def fillera(j, L, a, a_sum, a_known, l, l_sum, l_known):
	for i in range (0,n):
		if(L[i,j]<= -0.1):
			aleft = np.maximum(a[0,j]-a_sum[0,j], 0)
			print 'aleft', aleft
			lleft = np.maximum(l[0,i]-l_sum[0,i], 0)
			print 'lleft', lleft
			if(aleft < lleft):
				L[i,j] = (aleft)
				a_known[0,j] = a_known[0,j]+1
				a_sum[0,j] = a_sum[0,j]+L[i,j]
				l_known[0,i] = l_known[0,i]+1
				l_sum[0,i] = l_sum[0,i]+L[i,j]
			else:
				L[i,j] = (lleft)
				a_known[0,j] = a_known[0,j]+1
				a_sum[0,j] = a_sum[0,j]+L[i,j]
				l_known[0,i] = l_known[0,i]+1
				l_sum[0,i] = l_sum[0,i]+L[i,j]
		if(l_known[0,i] == n-1):
			print i, j, 
			print L, a, a_sum, a_known, l, l_sum, l_known
			L, a, a_sum, a_known, l, l_sum, l_known = fillerl(i, L, a, a_sum, a_known, l, l_sum, l_known)
	return L, a, a_sum, a_known, l, l_sum, l_known

def fillerl(j, L, a, a_sum, a_known, l, l_sum, l_known):
	k = 0 #filler variable for filler functions
	for i in range (0,n):
		if(L[j,i]<=-0.1):
			aleft = a[0,j]-a_sum[0,j]
			print 'aleft', aleft
			lleft = l[0,i]-l_sum[0,i]
			print 'lleft', lleft
			if(aleft<lleft):
				L[j,i] = (aleft)
				a_known[0,i] = a_known[0,i]+1
				a_sum[0,i] = a_sum[0,i]+L[j,i]
				l_known[0,j] = l_known[0,j]+1
				l_sum[0,j] = l_sum[0,j]+L[j,i]
			else:
				L[j,i] = (lleft)
				a_known[0,i] = a_known[0,i]+1
				a_sum[0,i] = a_sum[0,i]+L[i,j]
				l_known[0,j] = l_known[0,j]+1
				l_sum[0,j] = l_sum[0,j]+L[j,i]
		if(a_known[0,i] == n-1):
			print i, j
			print L, a, a_sum, a_known, l, l_sum, l_known
			L, a, a_sum, a_known, l, l_sum, l_known = fillera(i, L, a, a_sum, a_known, l, l_sum, l_known)
	return L, a, a_sum, a_known, l, l_sum, l_known

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
			a_known[0,j] = a_known[0,j] + 1
			l_known[0,i] = l_known[0,i] + 1
			
#Fill in edges for the lower triangle
for i in range (0, n-1):
	for j in range (i+1, n):
		u=random.random()
		if(u<p):
			A[i,j] = 1
		else:
			m=m+1
			a_known[0,j] = a_known[0,j] + 1
			l_known[0,i] = l_known[0,i] + 1
			
#we have A
print 'A = ', A
print 'm = ', m
print 'The values that are known for assets are ', a_known
print 'The values that are known for liabilities are ', l_known

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
	print 'The lambda we chose is:', lam
	
#weight the adjacency matrix with lamda
	Sampler = lam*A

#fill in known values of matrix
L = -1*A
for j in range (0,n):
	if(a_known[0,j] == n-1):
		fillera(j, L, a, a_sum, a_known, l, l_sum, l_known)
	if(l_known[0,j] == n-1):
		fillerl(j, L, a, a_sum, a_known, l, l_sum, l_known)

i = 0
j = 0
while(dof>0):
	go = True
	print 'dof', dof, 'go', go, 'i', i
#sample and fill in the liabilities matrix degrees of freedom
	while(i<=n and go == True):
		print 'i', i
		while(j<=n):
			print 'j', j
			if(L[i,j] == -1):
				L[i,j] = np.random.exponential(lam)
				print 'Lij', L[i,j]
				dof = dof-1
				go = False
				break
			else:
				j = j+1
		i = i + 1
		
#fill in the known values of the matrix
	for k in range (0,n):
		print 'k', k
		if(a_known[0,k] == n-1):
			L, a, a_sum, a_known, l, l_sum, l_known = fillera(k, L, a, a_sum, a_known, l, l_sum, l_known)
		if(l_known[0,k] == n-1):
			L, a, a_sum, a_known, l, l_sum, l_known = fillerl(k, L, a, a_sum, a_known, l, l_sum, l_known)

#We have completed our Liabiities matrix!
print "The liabilities matrix is ", L

