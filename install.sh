#!/bin/bash

mkdir -p $HOME/.silky
mkdir -p $HOME/.silky/logs

venv $HOME/.silky/.venv
cp ./run.py $HOME/.silky/run.py
cp ./dist_beta/silky-0.6.0b20-py2.py3-none-any.whl

$HOME/.silky/.venv/bin/pip install $HOME/.silky/silky-0.6.0b20-py2.py3-none-any.whl
