import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,10,1500)
v = np.zeros(len(t))
m = np.zeros(len(t))
h = np.zeros(len(t))
n = np.zeros(len(t))
dt = 0.05
I = 10    # nanoAmpeire
Cm = 1.0 # micro F/Cm^2
ENa=50   # miliVolt
EK=-77   # miliVolt
El=-54.4 # miliVolt
g_Na=120 # mS/Cm^2
g_K=36   # mS/Cm^2
g_l=0.03 # mS/Cm^2


def alphaN(v):
    return 0.01*(v+50)/(1-np.exp(-(v+50)/10))

def betaN(v):
    return 0.125*np.exp(-(v+60)/80)

def alphaM(v):
    return 0.1*(v+35)/(1-np.exp(-(v+35)/10))

def betaM(v):
    return 4.0*np.exp(-0.0556*(v+60))

def alphaH(v):
    return 0.07*np.exp(-0.05*(v+60))

def betaH(v):
    return 1/(1+np.exp(-(0.1)*(v+30)))

v[0] = -65
m[0] = alphaM(v[0])/(alphaM(v[0])+betaM(v[0]))
n[0] = alphaN(v[0])/(alphaN(v[0])+betaN(v[0]))
h[0] = alphaH(v[0])/(alphaH(v[0])+betaH(v[0]))

for i in range(1,len(t)):
    
    k1 = dt*(alphaN(v[i-1])*(1-n[i-1])-betaN(v[i-1])*n[i-1])
    k2 = dt*(alphaN(v[i-1])*(1-(n[i-1]+0.5*k1))-betaN(v[i-1])*(n[i-1]+0.5*k1))
    k3 = dt*(alphaN(v[i-1])*(1-(n[i-1]+0.5*k2))-betaN(v[i-1])*(n[i-1]+0.5*k2))
    k4 = dt*(alphaN(v[i-1])*(1-(n[i-1]+k3)-betaN(v[i-1])*(n[i-1]+k3)))
    
    n[i] = n[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    k1 = dt*(alphaM(v[i-1])*(1-m[i-1])-betaM(v[i-1])*m[i-1])
    k2 = dt*(alphaM(v[i-1])*(1-(m[i-1]+0.5*k1))-betaM(v[i-1])*(m[i-1]+0.5*k1))
    k3 = dt*(alphaM(v[i-1])*(1-(m[i-1]+0.5*k2))-betaM(v[i-1])*(m[i-1]+0.5*k2))
    k4 = dt*(alphaM(v[i-1])*(1-(m[i-1]+k3)-betaM(v[i-1])*(m[i-1]+k3)))

    m[i] = m[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    k1 = dt*(alphaH(v[i-1])*(1-h[i-1])-betaH(v[i-1])*h[i-1])
    k2 = dt*(alphaH(v[i-1])*(1-(h[i-1]+0.5*k1))-betaH(v[i-1])*(h[i-1]+0.5*k1))
    k3 = dt*(alphaH(v[i-1])*(1-(h[i-1]+0.5*k2))-betaH(v[i-1])*(h[i-1]+0.5*k2))
    k4 = dt*(alphaH(v[i-1])*(1-(h[i-1]+k3)-betaH(v[i-1])*(h[i-1]+k3)))
    
    h[i] = h[i-1] + (1/6)*(k1 + 2*k2 + 2*k3 + k4)
    
    gNa = g_Na*h[i-1]*(m[i-1])**3
    gK = g_K*n[i-1]**4
    gl = g_l
    INa = gNa*(v[i-1]-ENa)
    IK = gK*(v[i-1]-EK)
    Il = gl*(v[i-1]-El)
    k1 = dt*((1./Cm)*(I-(INa+IK+Il)))
    k2 = dt*((1./Cm)*(I-(INa+IK+Il) + 0.5*k1))
    k3 = dt*((1./Cm)*(I-(INa+IK+Il) + 0.5*k2))
    k4 = dt*((1./Cm)*(I-(INa+IK+Il) + k3))
    
    v[i] = v[i-1] + (1./6.)*(k1 + 2.*k2 + 2.*k3 + k4)
    

#Plot the data
plt.figure(figsize=(10,12))
plt.legend(loc='upper left')
plt.title('Hodgkin Huxely Model Rung-Kutta method')
plt.subplot(2,1,1)
plt.plot(t,v,'b-',label='voltage')
plt.legend(loc='upper left')
plt.xlabel('time (ms)')
plt.ylabel('Voltage')
plt.subplot(2,1,2)
plt.plot(t,n,'y-')
plt.xlabel('time')
plt.plot(t,m,'m-')
plt.xlabel('time')
plt.plot(t,h,'r-')
plt.xlabel('time')
plt.ylabel('Gates')
plt.legend(['n channel', 'm channel', 'h channel'])
#plt.savefig('HH model Rung-Kutta method.png',transparent=True)
plt.show()
