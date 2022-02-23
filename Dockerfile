FROM pytorch/pytorch:1.7.1-cuda11.0-cudnn8-runtime

RUN apt update && apt install -y build-essential \
                                 tmux \
                                 vim \
                                 libglew-dev \
                                 git \
                                 cmake \
                                 xorg-dev 
RUN pip install numpy-quaternion \
                torch-scatter==2.0.7 \
                torch-sparse==0.6.9 \
                torch-geometric==1.4.3 \
                -f https://data.pyg.org/whl/torch-1.7.0+cu110.html

COPY . /RoboGrammar
WORKDIR /RoboGrammar

RUN git submodule update --init
RUN mkdir build
RUN cd build && \
    cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .. && \
    make -j24

RUN python3 examples/design_search/setup.py develop

RUN python3 build/examples/python_bindings/setup.py develop

CMD ["/bin/bash"]
