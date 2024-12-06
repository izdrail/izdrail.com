# Base image
FROM python:3.11-slim

LABEL maintainer="Stefan Bogdanel <stefan@izdrail.com>"

#ENV STUFF
ARG JAVA_VERSION=17

ARG NODEJS_VERSION=20
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
# General packages
RUN apt-get install -qy \
    apt-utils \
    locales \
    gnupg2 \
    build-essential \
    curl \
    nodejs \
    npm \
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


# Set locale
RUN locale-gen en_US.UTF-8 && update-locale

# Install Gradle
ENV GRADLE_HOME=/opt/gradle
RUN mkdir $GRADLE_HOME \
    && curl -sL https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o gradle-${GRADLE_VERSION}-bin.zip \
    && unzip -d $GRADLE_HOME gradle-${GRADLE_VERSION}-bin.zip
ENV PATH=$PATH:/opt/gradle/gradle-${GRADLE_VERSION}/bin

# Install pip packages and supervisord
RUN pip install --no-cache-dir --upgrade pip \
    && pip install supervisor pipx

# Install Lighthouse globally
RUN npm install -g lighthouse


# FRONTEND - TODO: Make this work

COPY frontend /home/frontend/
COPY frontend/package.json /home/frontend/package.json
WORKDIR /home/frontend/
RUN npm install --legacy-peer-deps

#Now copy to 


# Upgrade pip and install pipx
RUN pip install --no-cache-dir --upgrade pip \
    && pip install pipx \
    && pip install lxml[html_clean] \
    && pip install gnews \
    && pip install poetry

# Set up FastAPI app
WORKDIR /home/backend
COPY backend . 

RUN pip install --no-cache-dir --upgrade -r requirements.txt \
    && pip install fastapi-versioning pymupdf4llm python-multipart yake tls_client uvicorn litellm asent spacyfishing\
    && pip install instabot lighthouse-python-plus gnews \
    && python3 -m nltk.downloader -d /usr/local/share/nltk_data wordnet punkt stopwords vader_lexicon \
    && python3 -m spacy download en_core_web_md \
    && python3 -m textblob.download_corpora

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

