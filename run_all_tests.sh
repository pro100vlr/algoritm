#!/bin/bash 
start_dir=$(pwd)
for lab in lab{1..7};
do
lab_folder=$lab
echo -e "$lab_folder\n"
for script in $lab_folder/task*/tests/*.py
do
run_script=$(echo "$script" | rev | cut -c 4- | rev)
run_script1=${run_script//\//.}
echo "Runing $script"
python3 -m $run_script1
done

done
