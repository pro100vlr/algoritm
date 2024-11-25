#!/bin/bash 
start_dir=$(pwd)
for lab in lab{1..4};
do
lab_folder=$lab
echo "$lab_folder"
cd "$lab_folder"
for script in Task*/tests/*.py
do
run_script=$(echo "$script" | rev | cut -c 4- | rev)
run_script1=${run_script//\//.}
echo "Runing $script"
python3 -m $run_script1
done

cd "$start_dir"

done
