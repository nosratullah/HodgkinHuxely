import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def alpha_n(v):
    return 0.01*(v+50)/(1-np.exp(-(v+50)/10))
def beta_n(v):
    return 0.125*np.exp(-(v+60)/80)
def alpha_h(v):
    return 0.07*np.exp(-0.05*(v+60))
def beta_h(v):
    return 1/(1+np.exp(-(0.1)*(v+30.0)))
def alpha_m(v):
    return 0.1*(v+35.0)/(1-np.exp(-(v+35.0)/10.0))
def beta_m(v):
    return 4.0*np.exp(-0.0556*(v+60))

def HHmodel(x,t):
    I = 10
    v = x[0] #initial values
    m = x[1]
    h = x[2]
    n = x[3]

    Cm = 1.0 #microFarad
    E_Na=50 #miliVolt
    E_K=-77  #miliVolt
    E_l=-54 #miliVolt
    g_Na=120 #mScm-2
    g_K=36 #mScm-2
    g_l=0.03 #mScm-2
    Esyn = 4 #mScm-2

    def I_Na(v,m,h):
        return g_Na * m**3 * h * (v - E_Na)
    def I_K(v,n):
        return g_K * n**4 * (v - E_K)
    def I_L(v):
        return g_l * (v - E_l)

    dvdt = (I - I_Na(v,m,h) - I_K(v,n) - I_L(v))/Cm
    dmdt = alpha_m(v)*(1.0 - m) - beta_m(v)*m
    dhdt = alpha_h(v)*(1.0 - h) - beta_h(v)*h
    dndt = alpha_n(v)*(1.0 - n) - beta_n(v)*n
    return [dvdt,dmdt,dhdt,dndt]

v0 = -65.0
n0 = float(alpha_n(v0)/(alpha_n(v0)+beta_n(v0)))
h0 = float(alpha_h(v0)/(alpha_h(v0)+beta_h(v0)))
m0 = float(alpha_m(v0)/(alpha_m(v0)+beta_m(v0)))
x0 = [v0,m0,h0,n0]
t = np.linspace(0,100,1000)
x = odeint(HHmodel,x0,t)
voltage = x[:,0]
mchannels = x[:,1]
hchannels = x[:,2]
nchannels = x[:,3]

plt.figure(figsize=(20,15))
plt.subplot(311)
plt.plot(voltage,'r-',label='voltage')
plt.legend(loc='best')
plt.subplot(312)
plt.plot(voltage,nchannels,'g-.',label='phase plan');
plt.legend(loc='best')
plt.subplot(313)
plt.plot(nchannels,label='n channels')
plt.subplot(313)
plt.plot(hchannels,label='h channels')
plt.subplot(313)
plt.plot(mchannels,label='m channels')
plt.legend(loc='best')
plt.show()
