import nest
import nest.voltage_trace


nest.set_verbosity("M_WARNING")
nest.ResetKernel()
nest.SetKernelStatus({'resolution': 0.025})


nest.Install("izh2module")
neuron = nest.Create("izh2")
multimeter = nest.Create('multimeter', params={'record_from': ['V_m']})


nest.SetStatus(neuron, "I_e", 6.0)
nest.SetStatus(multimeter, [{"withgid": True}])

nest.Connect(multimeter, neuron)


nest.Simulate(1000.0)

dmm = nest.GetStatus(multimeter, 'events')[0]
Vms = dmm["V_m"]
ts = dmm["times"]

import sys
if not '-nogui' in sys.argv: 
    import pylab
    pylab.figure(2)
    pylab.plot(ts, Vms)
    pylab.show()
    
dat = open('izh2.dat','w')
print('Writing %s data points'%len(ts))
for i in range(len(ts)):
    dat.write('%s\t%s\n'%(ts[i],Vms[i]))
dat.close()
    
print('Finished simulation')

print('Done!')
