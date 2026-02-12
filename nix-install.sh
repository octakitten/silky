python3 -m venv .venv
.venv/bin/activate
hatchling build -t wheel
pip3 install dist/silky-*.whl
python3 -m run.py
