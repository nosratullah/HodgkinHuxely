import nest
import matplotlib.pyplot as plt

#Creating neurons
neuron1 = nest.Create("iaf_psc_alpha")
nest.SetStatus(neuron1,{"I_e":0.0})
neuron2 = nest.Create("iaf_psc_alpha")
multimeter1 = nest.Create("multimeter")
nest.SetStatus(multimeter1, {"withtime":True, "record_from":["V_m"]})
multimeter2 = nest.Create("multimeter")
nest.SetStatus(multimeter2, {"withtime":True, "record_from":["V_m"]})
nest.SetStatus(neuron2,{"I_e":360.0})
noise_ex = nest.Create("poisson_generator")
noise_ex = nest.Create("poisson_generator")
noise_in = nest.Create("poisson_generator")
nest.SetStatus(noise_ex, {"rate": 80000.0})
nest.SetStatus(noise_in, {"rate": 15000.0})

syn_dict_ex = {"weight": 1.2}
syn_dict_in = {"weight": -2.0}
nest.Connect(noise_ex, neuron1, syn_spec=syn_dict_ex)
nest.Connect(noise_in, neuron1, syn_spec=syn_dict_in)

synapse = {"weight":50.0}
#connecting neurons
nest.Connect(neuron1, neuron2, syn_spec = synapse)
nest.Connect(multimeter1,neuron1)
nest.Connect(multimeter2,neuron2)

nest.Simulate(1000.0)

dmm1 = nest.GetStatus(multimeter1)[0]
Vms1 = dmm1["events"]["V_m"]
ts1 = dmm1["events"]["times"]

dmm2 = nest.GetStatus(multimeter2)[0]
Vms2 = dmm2["events"]["V_m"]
ts2 = dmm2["events"]["times"]

# Plot the result
plt.plot(ts1,-Vms1,'r',label='neuron 1')
plt.plot(ts2,-Vms2,'b',label='neuron 2')
plt.legend(loc='best')
plt.savefig('connectedNeuron.png')
plt.show()
