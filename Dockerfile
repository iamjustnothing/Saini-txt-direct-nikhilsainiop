#bot made my NIKHIL SAINI...All of you known as....SAINI BOTS

#Don't change here otherwise Repo crashed

# Pyrofork uses PEP 604 union type annotations (for example, ``int | str``),
# which require Python 3.10 or newer. Keep the container aligned with runtime.txt.
FROM python:3.11.1-alpine3.17

# Set the working directory
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . .

# Install necessary dependencies
RUN apk add --no-cache \
    gcc \
    libffi-dev \
    musl-dev \
    ffmpeg openssl \
    aria2 \
    make \
    g++ \
    cmake && \
    wget -q https://github.com/axiomatic-systems/Bento4/archive/v1.6.0-639.zip && \
    unzip v1.6.0-639.zip && \
    cd Bento4-1.6.0-639 && \
    mkdir build && \
    cd build && \
    cmake .. && \
    make -j$(nproc) && \
    cp mp4decrypt /usr/local/bin/ &&\
    cd ../.. && \
    rm -rf Bento4-1.6.0-639 v1.6.0-639.zip

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir --upgrade -r sainibots.txt \
    && python3 -m pip install -U yt-dlp
    
# Set the command to run the application
CMD ["sh", "-c", "gunicorn app:app & python3 main.py"]
