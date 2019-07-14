import numpy as np
import matplotlib.pyplot as plt
import CoupledNeuronLib as HH
import scipy as sp

length = 10000
zeroVoltage = np.zeros(length)
#inputCurrent = np.ones(length)*4
#inputCurrent[1000:2000] = 10
#inputCurrent[2000::] = 3
#inputCurrent2 = np.ones(length)*5.46
noisyInput1 = np.ones(length)*7 + np.random.normal(0,3,length)
noisyInput2 = np.ones(length)*5 + np.random.normal(0,3,length)
preVoltage,preSyn = HH.HodgkinHuxley(noisyInput1,zeroVoltage)
postVoltage,postSyn = HH.HodgkinHuxley(noisyInput2,preVoltage)
plt.figure(figsize=(15,10))
plt.plot(preVoltage,'r',label='pre synaptic voltage');
#plt.plot(postVoltage,'b');
plt.plot(postSyn,'g-.',label='synaptic voltage');
plt.plot(postVoltage,'b',label='post synaptic voltage');
#plt.xlim(xmin=0)
plt.ylim(ymax=50)
plt.legend(loc='upper left');
plt.savefig('coupledNeuron.png',dpi=150)
plt.show()
