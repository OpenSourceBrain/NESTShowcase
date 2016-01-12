'''
NEST simulator compliant export for:

Components:
    fn1 (Type: fitzHughNagumoCell:  I=0.8 (dimensionless) SEC=1.0 (SI time))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=200.0 (SI time) step=0.01 (SI time))

'''
# Main NEST script for: fn1_flat

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