
# We're using Alpine Edge
FROM alpine:edge

#
# We have to uncomment Community repo for some packages
#
RUN sed -e 's;^#http\(.*\)/edge/community;http\1/edge/community;g' -i /etc/apk/repositories
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/testing' >> /etc/apk/repositories


RUN adduser -D myuser
USER myuser

#
# Installing Packages
#
RUN apk add --no-cache --update \
    coreutils \
    bash \
    build-base \
    bzip2-dev \
    curl \
    figlet \
    gcc \
    g++ \
    git \
    aria2 \
    util-linux \
    libevent \
    jpeg-dev \
    libffi-dev \
    libpq \
    libwebp-dev \
    libxml2 \
    libxml2-dev \
    libxslt-dev \
    linux-headers \
    musl \
    neofetch \
    openssl-dev \
    postgresql \
    postgresql-client \
    postgresql-dev \
    openssl \
    pv \
    jq \
    wget \
    python3 \
    python3-dev \
    py3-pip \
    readline-dev \
    sqlite \
    ffmpeg \
    sqlite-dev \
    sudo \
    chromium \
    chromium-chromedriver \
    zlib-dev \
    jpeg \
    zip \
    megatools \
    nodejs \
    openssh \
    iproute2 \
    freetype-dev


RUN python3 -m ensurepip \
    && pip3 install --upgrade pip setuptools \
    && pip3 install wheel \
    && rm -r /usr/lib/python*/ensurepip && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache


ADD ./heroku-exec.sh /app/.profile.d

#
# Clone repo and prepare working directory
#
RUN git clone -b master https://github.com/fosslife/grambot /root/grambot
WORKDIR /root/grambot

#
# Copies session and config (if it exists)
#
COPY ./sample.env ./tguserbot.session* ./.env* /root/grambot/


#
# Install requirements
#
RUN pip3 install --no-cache-dir -q -r requirements.txt
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
CMD bash heroku-exec.sh && python3 -m userbot