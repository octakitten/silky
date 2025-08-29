#!/bin/bash

#mkdir -p $HOME/.silky
#mkdir -p $HOME/.silky/logs

#venv $HOME/.silky/.venv
#cp ./run.py $HOME/.silky/run.py
#cp ./dist_beta/silky-0.6.0b20-py2.py3-none-any.whl

#$HOME/.silky/.venv/bin/pip install $HOME/.silky/silky-0.6.0b20-py2.py3-none-any.whl

echo "Creating a virtual env..."

python3 -m venv .venv

echo "Created a Python virtual environment."
echo "Installing Hatch..."

.venv/bin/pip3 install hatch

echo "Installed Hatch in virtual environment."
echo "Building the Silky package..."

FOLDER="dist/"
rm -f $FOLDER*.whl
rm -f $FOLDER*.tar.gz
.venv/bin/python3 -m hatch build -t wheel $FOLDER

echo "Built package in folder dist/"
echo "Installing Silky to virtual env..."

.venv/bin/pip3 uninstall silky -y
.venv/bin/pip3 install ${FOLDER}silky-*.whl

echo "Installed package Silky to virtual environment."
