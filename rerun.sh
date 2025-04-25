#!/bin/bash
source ~/coding/badaba/index/silky/.venv/bin/activate 
rm -f ./silky-*.whl
wget --no-cache https://github.com/octakitten/silky/releases/download/latest/silky-0.6.0b20-py2.py3-none-any.whl
pip3 uninstall silky -y
pip3 install silky-*.whl
python3 ~/coding/badaba/index/silky/run.py
