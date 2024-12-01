#!/bin/bash 
for script in Task*/src/*.py
do
run_script=$(echo "$script" | rev | cut -c 4- | rev)
run_script1=${run_script//\//.}
echo "Runing $script"
python3 -m $run_script1

done
