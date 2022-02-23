FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-runtime

RUN pip install numpy-quaternion \
                torch-scatter \
                torch-sparse \
                torch-cluster \
                torch-spline-conv \
                torch-geometric \
                -f https://data.pyg.org/whl/torch-1.10.0+cu113.html
RUN apt update && apt install -y tmux \
                                 vim \
                                 libglew-dev

COPY . /RoboGrammar
WORKDIR /RoboGrammar

RUN git submodule update --init
RUN mkdir build
RUN cd build && \
    cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo .. && \
    make -j24
CMD ["/bin/bash"]
