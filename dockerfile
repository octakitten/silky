FROM nvidia/cuda:12.5.1-runtime-ubuntu24.04
RUN apt-get update
RUN apt-get install -y python3 python3-pip python3-venv curl clang git gh zip
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN /venv/bin/pip3 install --upgrade pip
RUN /venv/bin/pip3 install --upgrade hatch
