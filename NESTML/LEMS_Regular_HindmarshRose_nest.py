'''
NEST simulator compliant export for:

Components:
    hr_regular (Type: hindmarshRoseCell:  a=1.0 (dimensionless) b=3.0 (dimensionless) c=-3.0 (dimensionless) d=5.0 (dimensionless) I=5.0 (dimensionless) r=0.002 (dimensionless) s=4.0 (dimensionless) x1=-1.3 (dimensionless) x0=-1.3 (dimensionless) y0=-1.0 (dimensionless) z0=1.0 (dimensionless) SEC=1.0 (SI time))
    net1 (Type: network)
    sim1 (Type: Simulation:  length=2000.0 (SI time) step=0.005 (SI time))

'''
# Main NEST script for: hr_regular_flat

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