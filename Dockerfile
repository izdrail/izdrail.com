# Base image
FROM python:3.11

LABEL maintainer="Stefan Bogdanel <stefan@izdrail.com>"

#ENV STUFF
ARG JAVA_VERSION=17

ARG NODEJS_VERSION=18
# See https://developer.android.com/studio/index.html#command-tools
ARG ANDROID_SDK_VERSION=11076708
# See https://developer.android.com/tools/releases/build-tools
ARG ANDROID_BUILD_TOOLS_VERSION=34.0.0
# See https://developer.android.com/studio/releases/platforms
ARG ANDROID_PLATFORMS_VERSION=34
# See https://gradle.org/releases/
ARG GRADLE_VERSION=8.2.1
# See https://www.npmjs.com/package/@ionic/cli
ARG IONIC_VERSION=7.2.0
# See https://www.npmjs.com/package/@capacitor/cli
ARG CAPACITOR_VERSION=6.0.0

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=en_GB.UTF-8

## Start the logic of ionic 
RUN apt-get update -q

RUN apt-get purge -qy \
    cmdtest

RUN apt-get install -qy \
    apt-utils \
    locales \
    gnupg2 \
    build-essential \
    curl \
    nodejs \
    npm 


# FRONTEND - TODO: Make this work

COPY frontend /home/frontend/
COPY frontend/package.json /home/frontend/package.json
WORKDIR /home/frontend/
RUN npm install
RUN npm run build


# General packages
RUN apt-get install -qy \
    apt-utils \
    locales \
    gnupg2 \
    build-essential \
    curl \
    nodejs \
    npm \
    yarn \
    mlocate \
    net-tools \
    software-properties-common \
    maven \
    usbutils \
    git \
    unzip \
    p7zip p7zip-full \
    python3 \
    openjdk-${JAVA_VERSION}-jre \
    openjdk-${JAVA_VERSION}-jdk


RUN curl -sL https://deb.nodesource.com/setup_${NODEJS_VERSION}.x | bash - \
    && apt-get update -q && apt-get install -qy nodejs


# Install pip packages and supervisord
RUN pip install --no-cache-dir --upgrade pip \
    && pip install supervisor pipx

# Install Lighthouse globally
RUN npm install -g lighthouse
#RUN curl -sSL install.astronomer.io | bash -s



# Upgrade pip and install pipx
RUN pip install --no-cache-dir --upgrade pip \
    && pip install pipx \
    && pip install lxml[html_clean] \
    && pip install gnews \
    && pip install poetry

# Set up backend api
WORKDIR /home/backend
COPY backend . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    && pip install fastapi-versioning pymupdf4llm python-multipart yake tls_client uvicorn litellm \
    && pip install instabot lighthouse-python-plus gnews \
    && python3 -m nltk.downloader -d /usr/local/share/nltk_data wordnet punkt stopwords vader_lexicon \
    && python3 -m spacy download en_core_web_md \
    && python3 -m textblob.download_corpora



WORKDIR /home/magazines
COPY magazines  .

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean \
    && updatedb

# Copy Supervisor configuration
COPY docker/supervisord.conf /etc/supervisord.conf


# Expose application ports
EXPOSE 12000 12001 

# Run application
ENTRYPOINT ["supervisord", "-c", "/etc/supervisord.conf", "-n"]

