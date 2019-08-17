# HodgkinHuxely-Spiking
A Model to simulate neuronal spiking based on Hodgkin Huxley model

The Hodgkin–Huxley model, or conductance-based model, is a mathematical model that describes 
how action potentials in neurons are initiated and propagated. It is a set of nonlinear differential equations 
that approximates the electrical characteristics of excitable cells such as neurons and cardiac myocytes.
Alan Lloyd Hodgkin and Andrew Fielding Huxley described the model in 1952 to explain the ionic mechanisms underlying the initiation and propagation of action potentials in the squid giant axon.[1] They received the 1963 Nobel Prize in Physiology or Medicine for this work.

![finalPlot](https://user-images.githubusercontent.com/13776994/57675235-957fc100-7636-11e9-98be-a7415e59da7c.png)

# Noisy Input
Neuronal noise or neural noise refers to the random intrinsic electrical fluctuations within neuronal networks. These fluctuations are not associated with encoding a response to internal or external stimuli and can be from one to two orders of magnitude.[1] Most noise commonly occurs below a voltage-threshold that is needed for an action potential to occur, but sometimes it can be present in the form of an action potential; for example, stochastic oscillations in pacemaker neurons in suprachiasmatic nucleus are partially responsible for the organization of circadian rhythms.[2][3]

![spikes_random_noise](https://user-images.githubusercontent.com/13776994/58783163-88327280-85f5-11e9-8c39-f9da61eb33b3.png)


# Coupled Neuron with Noisy Inputs
Ephaptic coupling is a form of communication within the nervous system and is distinct from direct communication systems like electrical synapses and chemical synapses. It may refer to the coupling of adjacent (touching) nerve fibers caused by the exchange of ions between the cells, or it may refer to coupling of nerve fibers as a result of local electric fields.[5] In either case ephaptic coupling can influence the synchronization and timing of action potential firing in neurons. Myelination is thought to inhibit ephaptic interactions.[6]

![coupledNeuron](https://user-images.githubusercontent.com/13776994/61179897-d2aa0480-a621-11e9-83ab-3955643544dd.png)

# Model 2:[7]
<img width="889" alt="Screen Shot 2019-08-14 at 11 49 32" src="https://user-images.githubusercontent.com/13776994/63001782-9ddfd600-be89-11e9-97f0-9592ff27a9b5.png">

![coupledNeuron](https://user-images.githubusercontent.com/13776994/63001573-2611ab80-be89-11e9-873d-c0e69a54b8fd.png)

# Connected Neuron using Nest Library(LIF model):
![connectedNeuron](https://user-images.githubusercontent.com/13776994/63207613-661d9c00-c0de-11e9-8594-e5db80b8de35.png)


# refrences
[1]  Hodgkin AL, Huxley AF (August 1952). "A quantitative description of membrane current and its application to conduction and excitation in nerve". The Journal of Physiology. 117 (4): 500–44. doi:10.1113/jphysiol.1952.sp004764. PMC 1392413. PMID 12991237.

[2]  Jacobson, G. A. (2005). "Subthreshold voltage noise of rat neocortical pyramidal neurones". J Physiol. 564 (Pt 1): 145–160. doi:10.1113/jphysiol.2004.080903. PMC 1456039. PMID 15695244.

[3]  Ko, C. H. (2010). "Emergence of Noise-Induced Oscillations in the Central Circadian Pacemaker". PLOS Biology. 8 (10): e1000513. doi:10.1371/journal.pbio.1000513. PMC 2953532. PMID 20967239.

[4]  Mazzoni, E. O. (2005). "Circadian Pacemaker Neurons Transmit and Modulate Visual Information to Control a Rapid Behavioral Response". Neuron. 45 (2): 293–300. doi:10.1016/j.neuron.2004.12.038. PMID 15664180.

[5]  Aur D., Jog, MS. (2010) Neuroelectrodynamics: Understanding the brain language, IOS Press, doi:10.3233/978-1-60750-473-3-i

[6]  Hartline DK (May 2008). "What is myelin?". Neuron Glia Biol. 4 (2): 153–63. doi:10.1017/S1740925X09990263. PMID 19737435.

[7]  Flexible resonance in prefrontal networks with strong feedback inhibition, https://doi.org/10.1371/journal.pcbi.1006357
