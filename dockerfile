FROM nvidia/cuda:12.5.1-runtime-ubuntu24.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv curl clang git gh
RUN python3 -m venv /venv
RUN /venv/bin/python -m pip install hatch
RUN ln -s /venv/bin/python3 /usr/bin/python
