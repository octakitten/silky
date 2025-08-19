.venv/bin/pip3 uninstall silky -y
.venv/bin/pip3 install ./dist_beta/*.whl
.venv/bin/pytest
