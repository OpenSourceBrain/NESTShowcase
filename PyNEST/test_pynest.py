import nest

print("Test 1: NEST version: %s"% (nest.__version__ if hasattr(nest,'__version__') else nest.version()))

import numpy as np

neuron = nest.Create('aeif_cond_alpha_multisynapse')
nest.SetStatus(neuron, {"V_peak": 0.0, "a": 4.0, "b":80.5})
nest.SetStatus(neuron, {'E_rev':[0.0, 0.0, 0.0, -85.0],
                        'tau_syn':[1.0, 5.0, 10.0, 8.0]})

spike = nest.Create('spike_generator', params = {'spike_times':
                                                np.array([10.0])})

voltmeter = nest.Create('voltmeter', 1)

delays=[1.0, 300.0, 500.0, 700.0]
w=[1.0, 1.0, 1.0, 1.0]
for syn in range(4):
    nest.Connect(spike, neuron, syn_spec={'receptor_type': 1 + syn,
                                          'weight': w[syn],
                                          'delay': delays[syn]})

nest.Connect(voltmeter, neuron)

nest.Simulate(1000.0)
dmm = nest.GetStatus(voltmeter)[0]
Vms = dmm["events"]["V_m"]
ts = dmm["events"]["times"]

f = open('V_m.dat','w')
for ti in range(len(ts)):
    f.write('%s\t%s\n'%(ts[ti]/1000.,Vms[ti]/1000.))
f.close()

import pylab
import sys
if not '-nogui' in sys.argv:
    pylab.figure(2)
    pylab.plot(ts, Vms)
    pylab.show()

print('Finished simulation')
