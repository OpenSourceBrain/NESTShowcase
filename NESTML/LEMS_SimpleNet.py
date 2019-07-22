'''
NEST simulator compliant export for:

Components:
    iaf (Type: iafCell:  leakConductance=1.0E-8 (SI conductance) leakReversal=-0.065 (SI voltage) thresh=-0.05 (SI voltage) reset=-0.07 (SI voltage) C=2.0000000000000003E-10 (SI capacitance))
    null (Type: notes)
    null (Type: property)
    syn0 (Type: expTwoSynapse:  tauRise=5.0E-4 (SI time) tauDecay=0.01 (SI time) peakTime=0.0015767011966073639 (SI time) waveformFactor=1.232399909181873 (dimensionless) gbase=2.0E-9 (SI conductance) erev=0.0 (SI voltage))
    poissonFiringSyn (Type: poissonFiringSynapse:  averageRate=150.0 (SI per_time) averageIsi=0.006666666666666667 (SI time))
    SimpleNet (Type: networkWithTemperature:  temperature=305.15 (SI temperature))
    Sim_SimpleNet (Type: Simulation:  length=0.5 (SI time) step=2.5E-5 (SI time))


    This NEST file has been generated by org.neuroml.export (see https://github.com/NeuroML/org.neuroml.export)
         org.neuroml.export  v1.5.4
         org.neuroml.model   v1.5.4
         jLEMS               v0.9.9.1

'''
# Main NEST script for: SimpleNet

#   
#   PLEASE NOTE: This export is far from complete
#              
#   Waiting for an initial reference example of NESTML....
#   

import nest
import nest.voltage_trace
nest.set_verbosity("M_WARNING")
nest.ResetKernel()

neuron = nest.Create("iaf_neuron")
voltmeter = nest.Create("voltmeter")