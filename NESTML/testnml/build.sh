set -e

rm -rf report target
nestml --input_path  /home/docker/local  --module_name nmlmodule
cd target
ls -alt
cmake -Dwith-nest=/home/docker/env/neurosci/bin/nest-config .
make 
make install