from pylab import *
# 1. Data Gathering
from pandas .io. data import *
AAPL=DataReader('AAPL', 'yahoo', start ='01/01/2006')
# 2. Data Analysis
from pandas import*
AAPL['Ret']= log(AAPL['Close']/AAPL['Close'].shift(1))
# 3. Plotting
subplot(211)
AAPL['Close'].plot(); ylabel('Index Level')
subplot(212)
AAPL['Ret'].plot(); ylabel('Log Returns')
# 4. Monte Carlo Simulation
S0=AAPL['Close'][-1]
vol=std( AAPL ['Ret'])* sqrt (252 )
r=0.025; K=S0*1.1; T=1.0; M=50; dt=T/M; I= 10000
S=zeros((M+1,I )); S[0 ,:]= S0
for t in range (1,M+1):
	ran=standard_normal(I)
	S[t ,:]= S[t-1 ,:]* exp ((r-vol **2/2)* dt+ vol * sqrt (dt )* ran)
# 5. Option Valuation
V0=exp(-r*T)*sum(maximum(S[-1]-K,0))/I
print "Call Value %8.3f" %V0
# 6. Data Storage
h5file=HDFStore('AAPL .h5'); h5file['AAPL']=AAPL; h5file.close()
