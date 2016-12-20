set -e

cd NeuroML2

jnml LEMS_SimpleNet.xml -nest 

jnml LEMS_NML2_Ex9_FN.xml -nest 

jnml LEMS_2007One.xml -nest 

jnml LEMS_Regular_HindmarshRose.xml -nest 

rm -rf *.json

mv LEMS*.py *.nestml ../NESTML





