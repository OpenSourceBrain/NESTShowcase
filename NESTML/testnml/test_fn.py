import nest
import nest.voltage_trace

import sys

nest.set_verbosity("M_WARNING")
nest.ResetKernel()
nest.SetKernelStatus({'resolution': 0.1})


if '-izh1' in sys.argv: 
    neuron = nest.Create("izhikevich")
else:
    nest.Install("nmlmodule")
    neuron = nest.Create("fn1")

print(type(neuron))
multimeter = nest.Create('multimeter', params={'record_from': ['V','W']})


nest.SetStatus(multimeter, [{"withgid": True}])

nest.Connect(multimeter, neuron)


nest.Simulate(200000)

dmm = nest.GetStatus(multimeter, 'events')[0]
Vs = dmm["V"]
Ws = dmm["W"]
ts = dmm["times"]

if not '-nogui' in sys.argv: 
    import pylab
    pylab.figure(2)
    pylab.plot(ts, Vs)
    pylab.show()
    
dat = open('fn.dat','w')
print('Writing %s data points'%len(ts))
for i in range(len(ts)):
    dat.write('%s\t%s\t%s\n'%(ts[i],Vs[i],Ws[i]))
dat.close()
    
print('Finished simulation')

print('Done!')
