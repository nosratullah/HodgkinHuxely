import numpy as np

def HodgkinHuxley(I,preVoltage):

    #holders
    v = []
    m = []
    h = []
    n = []
    s = [] #synaptic channel
    Isynlist = []
    dt = 0.05
    t = np.linspace(0,10,len(I))

    #constants
    Cm = 1.0 #microFarad
    ENa=50 #miliVolt
    EK=-77  #miliVolt
    El=-54 #miliVolt
    E_ampa = 0 #miliVolt
    g_Na=120 #mScm-2
    g_K=36 #mScm-2
    g_l=0.03 #mScm-2
    g_syn = 0.3
    t_d = 2 #ms Decay time
    t_r = 0.4 #ms Raise time
    Tij = 0 #ms time delay
    #Define functions
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

    def H_pre(preV):
        return 1 + np.tanh(preV)

    #Initialize the voltage and the channels :
    v.append(-60)
    m0 = alphaM(v[0])/(alphaM(v[0])+betaM(v[0]))
    n0 = alphaN(v[0])/(alphaN(v[0])+betaN(v[0]))
    h0 = alphaH(v[0])/(alphaH(v[0])+betaH(v[0]))
    #s0 = alpha_s(preVoltage[0])/(alpha_s(preVoltage[0])+beta_s(preVoltage[0]))
    s0 = 0

    #t.append(0)
    m.append(m0)
    n.append(n0)
    h.append(h0)
    s.append(s0)

    if (type(preVoltage)==int):
        preVoltage = np.zeros(len(I)) #check if preVoltage exists or not

    #solving ODE using Euler's method:
    for i in range(1,len(t)):
        m.append(m[i-1] + dt*((alphaM(v[i-1])*(1-m[i-1]))-betaM(v[i-1])*m[i-1]))
        n.append(n[i-1] + dt*((alphaN(v[i-1])*(1-n[i-1]))-betaN(v[i-1])*n[i-1]))
        h.append(h[i-1] + dt*((alphaH(v[i-1])*(1-h[i-1]))-betaH(v[i-1])*h[i-1]))
        s.append(s[i-1] + dt * (H_pre(preVoltage[i-1])*((1-s[i-1]/t_r))-(s[i-1]/t_d)))
        gNa = g_Na * h[i-1]*(m[i-1])**3
        gK = g_K*n[i-1]**4
        gl = g_l
        INa = gNa*(v[i-1]-ENa)
        IK = gK*(v[i-1]-EK)
        Il = gl*(v[i-1]-El)
        #Synaptic Current comes from the pre neuron
        Isyn = -0.1 * s[i-1] * (v[i-1] - E_ampa)
        #making a list for Synaptic currents for plotting
        Isynlist.append(Isyn)
        v.append(v[i-1]+(dt)*((1/Cm)*(I[i-1]-(INa+IK+Il+Isyn))))

    return v,Isynlist
