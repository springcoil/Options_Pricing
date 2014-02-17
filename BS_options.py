## Valuation of European Put Option  'IBM130316P00145000' using Yahoo Finance data Monday 11th of March
# by Monte Carlo Simulation
#
from numpy import *
from numpy . random import standard_normal , seed
from time import time
t0= time ()
## Parameters -- American Put Option
S0 = 145.00 # initial stock level
K = 209.28 # strike price
T = 1.0 # time -to - maturity
vol = 40 # volatility
r = 0.06 # short rate
## Simulation Parameters
seed ( 150000 ) # seed for Python RNG
M = 50 # time steps
I = 50000 # simulation paths
dt = T/M # length of time interval
df = exp (-r*dt) # discount factor per time interval
## Index Level Path Generation
S= zeros ((M+1,I),'d') # index value matrix
S[0 ,:]= S0 # initial values
for t in range (1,M+1,1): # stock price paths
	ran = standard_normal (I) # pseudo - random numbers
	S[t ,:]= S[t-1 ,:]* exp ((r-vol **2/2)* dt+ vol * ran * sqrt (dt ))
## Valuation
h= maximum (K-S[-1],0) # inner values at maturity
V0= exp (-r*T)* sum(h)/I # MCS estimator
## Output
print " Time elapsed in Seconds %8.3f" %( time ()- t0)
print " ----------------------------------------"
print " European Put Option Value of IBM Option %8.3f" %V0
print " ----------------------------------------"
