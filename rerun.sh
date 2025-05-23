#!/bin/bash
## bash script for handling the build process locally rather than externally with github actions
## mostly used for debugging

## build the package
echo  "Building Silky package"
FOLDER="dist_beta/"
rm -f $FOLDER*.whl
rm -f $FOLDER*.tar.gz
hatch build -t wheel $FOLDER
echo "Built package!"

## install the package
.venv/bin/pip3 uninstall silky -y
.venv/bin/pip3 install dist_beta/silky-*.whl

## run the package test script and print to a logfile
printf -v today '%(%Y%m%d)T' -1
num=1
filename=$today-log.txt
while [ -e "$filename" ]; do
	printf -v filename '%s-%01d-log.txt' "$today" "$(( ++num ))"
done
echo 'Printing to logfile "%s"' "$filename"
folder="logs/"
mkdir -p "$folder"
.venv/bin/python3 run.py > "$folder$filename"
