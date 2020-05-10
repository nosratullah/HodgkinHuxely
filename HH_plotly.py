import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go


def HHmodel(mean = 0, length = 500, area = 1.0, mode = 'noisy', std = 5):

    if (mode == 'noisy'):
        I = np.random.normal(mean,std,length)
    if (mode == 'clean'):
        I = np.ones(length) * mean
    v = np.zeros(length)
    m = np.zeros(length)
    h = np.zeros(length)
    n = np.zeros(length)
    dt = 0.05
    t = np.linspace(0,100,length)

    #meandiff_sq = np.zeros(length)

    #constants
    Cm = area#microFarad
    ENa=50 #miliVolt
    EK=-77  #miliVolt
    El=-54 #miliVolt
    g_Na=120*area #mScm-2
    g_K=36*area #mScm-2
    g_l=0.03*area #mScm-2

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
    v[0] = -60
    m[0] = alphaM(v[0])/(alphaM(v[0])+betaM(v[0]))
    n[0] = alphaN(v[0])/(alphaN(v[0])+betaN(v[0]))
    h[0] = alphaH(v[0])/(alphaH(v[0])+betaH(v[0]))

    #solving ODE using Euler's method:
    for i in range(1,length):
        m[i] = m[i-1] + dt*((alphaM(v[i-1])*(1-m[i-1]))-betaM(v[i-1])*m[i-1])
        n[i] = n[i-1] + dt*((alphaN(v[i-1])*(1-n[i-1]))-betaN(v[i-1])*n[i-1])
        h[i] = h[i-1] + dt*((alphaH(v[i-1])*(1-h[i-1]))-betaH(v[i-1])*h[i-1])
        gNa = g_Na * h[i-1]*(m[i-1])**3
        gK=g_K*n[i-1]**4
        gl=g_l
        INa = gNa*(v[i-1]-ENa)
        IK = gK*(v[i-1]-EK)
        Il= gl * (v[i-1]-El)
        v[i] = v[i-1] + (dt*((1/Cm)*(I[i-1]-(INa+IK+Il))))

    return v

# Create figure
fig = go.Figure()

# Add traces, one for each slider step
for step in np.arange(1, 20, 0.1):
    fig.add_trace(
        go.Scatter(
            visible=False,
            line=dict(color="#00CED1", width=1),
            name= "I: "+ str(step),
            #x = np.arange(0, 20, 0.1),
            #y = np.sin(step * np.arange(0, 10, 0.01))))
            y = HHmodel(step, length =500, mode = 'clean')))

# Make 10th trace visible
fig.data[10].visible = True

# Create and add slider
steps = []
for i in range(len(fig.data)):
    step = dict(
        method="update",
        args=[{"visible": [False] * len(fig.data)},
              {"title": "Input Current (mA): " + str(i/10)}],  # layout attribute
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=10,
    currentvalue={"prefix": "Input Current: "},
    pad={"t": 50},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.show()
