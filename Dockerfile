FROM python:3.12-slim AS build-stage

WORKDIR /opt/app

# Install dependencies
RUN apt-get -y update && \
    apt-get install -y build-essential git cmake libssl-dev

# Get liboqs
RUN git clone --depth 1 --branch main https://github.com/open-quantum-safe/liboqs

# Install liboqs with stateful-signature algorithms enabled
RUN cmake -S liboqs -B liboqs/build \
        -DBUILD_SHARED_LIBS=ON \
        -DOQS_ENABLE_SIG_STFL_LMS=ON \
        -DOQS_ENABLE_SIG_STFL_XMSS=ON \
        -DOQS_HAZARDOUS_EXPERIMENTAL_ENABLE_SIG_STFL_KEY_SIG_GEN=ON && \
    cmake --build liboqs/build --parallel 4 && \
    cmake --build liboqs/build --target install

# Get liboqs-python
RUN git clone --depth 1 --branch main https://github.com/open-quantum-safe/liboqs-python.git

# Install liboqs-python
RUN cd liboqs-python && pip install -U pip setuptools && pip install --no-cache-dir . && cd $HOME

ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib
COPY pqc pqc
COPY main.py main.py
COPY requirements.txt .
COPY setup.py .
COPY client.py .

RUN pip install --no-cache-dir -e .

EXPOSE 5000

CMD ["gunicorn", "--workers", "8", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:5000", "main:app"]