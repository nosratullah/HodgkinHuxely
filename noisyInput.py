import numpy as np
import matplotlib.pyplot as plt


def HHmodel(I,length):
    #holders
    v = []
    m = []
    h = []
    n = []
    dt = 0.05
    t = np.linspace(0,100,length)

    #constants
    Cm = 1.0 #microFarad
    ENa=50 #miliVolt
    EK=-77  #miliVolt
    El=-54 #miliVolt
    g_Na=120 #mScm-2
    g_K=36 #mScm-2
    g_l=0.03 #mScm-2

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

    #Initialize the voltage and the channels :
    v.append(-60)
    m0 = alphaM(v[0])/(alphaM(v[0])+betaM(v[0]))
    n0 = alphaN(v[0])/(alphaN(v[0])+betaN(v[0]))
    h0 = alphaH(v[0])/(alphaH(v[0])+betaH(v[0]))

    #t.append(0)
    m.append(m0)
    n.append(n0)
    h.append(h0)

    #solving ODE using Euler's method:
    for i in range(1,len(t)):
        m.append(m[i-1] + dt*((alphaM(v[i-1])*(1-m[i-1]))-betaM(v[i-1])*m[i-1]))
        n.append(n[i-1] + dt*((alphaN(v[i-1])*(1-n[i-1]))-betaN(v[i-1])*n[i-1]))
        h.append(h[i-1] + dt*((alphaH(v[i-1])*(1-h[i-1]))-betaH(v[i-1])*h[i-1]))
        gNa = g_Na * h[i-1]*(m[i-1])**3
        gK=g_K*n[i-1]**4
        gl=g_l
        INa = gNa*(v[i-1]-ENa)
        IK = gK*(v[i-1]-EK)
        Il=gl*(v[i-1]-El)
        v.append(v[i-1]+(dt)*((1/Cm)*(I[i-1]-(INa+IK+Il))))
        #v.append(v[i-1]+(dt)*((1/Cm)*(I-(INa+IK+Il))))
    return v,t



spikeEvents = []  #timing each spike
length = 1000000*5  #the time period
barcode = np.zeros(length)
noisyI = np.random.normal(0,9,length)
v,t = HHmodel(noisyI,length)
#to count the spikes:
for i in range(1,len(v)):
    if (v[i-1] < 0 and v[i] > 0):
        spikeEvents.append(round(t[i],3))

timeDistribution = [] #to distributing time
for i in range(len(spikeEvents)):
    timeDistribution.append(spikeEvents[i]-spikeEvents[i-1])
#print(spikeEvents)
max(timeDistribution)
timeDistribution = sorted(timeDistribution)
timeDistribution[0] = 0
#plt.scatter(range(len(timeDistribution)),timeDistribution);
len(spikeEvents)
x = range(len(spikeEvents))
np.mean(spikeEvents)
np.std(spikeEvents)
round((np.std(spikeEvents)/np.mean(spikeEvents)),4)
np.var(spikeEvents)

plt.figure(figsize=(20,30))
plt.legend(loc='upper left')
plt.title('Hodgkin Huxely Spike Model with noisy input')
plt.subplot(3,1,1)
plt.plot(t,v,label='voltage with noisy input');
plt.ylabel('voltage')
plt.legend(loc='upper left')
plt.title('Hodgkin Huxely Spike Model with noisy input')
plt.subplot(3,1,2)
plt.eventplot(spikeEvents,label='Spike events',colors='red');
plt.legend(loc='upper left')
plt.xlabel('time (ms)')
plt.ylabel('Spikes')
plt.subplot(3,1,3)
plt.hist(timeDistribution,50,label='spike time distribution')
plt.legend(loc='upper left');
plt.savefig('spikes_random_noise.png')
plt.show()
print('Done.')
