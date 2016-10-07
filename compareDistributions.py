#compareDistributions.py
#Natalie Wellen
#10/07/16
import random
import numpy as np
import matplotlib.pyplot as plt
import expoDistribution as expo

#This file is a script to help understand the distribution proposed by Cont and Kokholm 
#compared to the distribution proposed by Duffie and Zhu for bank exposures
#   I currently am unsure how the notional amount plays a role in the distributions. Do either
#of these distributions exclude that case? Also Cont and Kokholm only allow positive or zero values
#for the exposure amounts, how does that affect their calculations? It also seems that they ned to
#modify their values so that we have X_ij = -X_ji


#Asset class one is CDS
#betak is the measure of illiquidity in the market
beta1 = .5 
#zk is the vector of gross notionals where the i'th entry is the i'th bank's
z1 = np.array([120.,234.,103.,98.,67.,68.,20.])
#l is the number of samples to be plotted in a histogram
l = 1000

print "The total gross notionals for each bank are: ", z1
n, fracs = expo.exposureFrac(z1, beta1)
print "Our estimated amount of gross notionals traded between two banks is:"
print fracs
expo.histCompare(z1, beta1, l, expo.duffie, expo.cont, True)		
'''
xDuffie = duffie(n, f, True)
print"duffie:"
print xDuffie
xCont = cont(n,f, True)
print"Cont"
print xCont
compare = np.absolute(xCont) < np.absolute(xDuffie)
true = np.sum(compare)
print "Cont and Kokholm's measure is less than Duffie and Zhus's", true, "out of", n*n-n, "times."
'''

#I have noticed the distributions are about the same, so why change them at all? 
#and also that our tails end up being just about (mostly under) 4x the 
#estimated notional trade between tow banks