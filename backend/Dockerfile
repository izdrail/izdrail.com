# Base image
FROM python:3.11
#FROM ubuntu:latest

LABEL maintainer="Stefan Bogdanel <stefan@izdrail.com>"

# Install dependencies
RUN apt update && apt install -y \
    curl \
    nodejs \
    npm \
    mlocate \
    net-tools \
    software-properties-common \
    openjdk-17-jdk \
    maven \
    chromium \
    && apt-get clean

# Install pip packages and supervisord
RUN pip install --no-cache-dir --upgrade pip \
    && pip install supervisor pipx

# Install Lighthouse globally
RUN npm install -g lighthouse

# Add a non-root user `osint`
RUN useradd -ms /bin/bash osint

# Clone and build Spiderfoot
WORKDIR /home/osint
RUN git clone https://github.com/smicallef/spiderfoot.git
WORKDIR /home/osint/spiderfoot
RUN pip install -r requirements.txt
RUN chown -R osint:osint /home/osint/spiderfoot

# Clone and build BBOT
WORKDIR /home/osint
RUN git clone https://github.com/blacklanternsecurity/bbot.git
WORKDIR /home/osint/bbot
RUN pipx install bbot
RUN chown -R osint:osint /home/osint/bbot

# Clone and build Skraper
WORKDIR /home/osint
RUN git clone https://github.com/sokomishalov/skraper.git
WORKDIR /home/osint/skraper
RUN ./mvnw clean package -DskipTests=true \
    && mkdir -p /usr/local/skraper \
    && cp /home/osint/skraper/cli/target/cli.jar /usr/local/skraper/
RUN echo '#!/bin/bash\njava -jar /usr/local/skraper/cli.jar "$@"' > /usr/local/bin/skraper \
    && chmod +x /usr/local/bin/skraper
RUN chown -R osint:osint /home/osint/skraper

# Install Python packages
COPY ./requirements.txt /home/osint/app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /home/osint/app/requirements.txt \
    && pip install pymupdf4llm instabot python-multipart lighthouse-python-plus yake tls_client uvicorn gnews \
    && python3 -m nltk.downloader -d /usr/local/share/nltk_data wordnet punkt stopwords vader_lexicon \
    && python3 -m spacy download en_core_web_md \
    && python3 -m textblob.download_corpora
RUN chown -R osint:osint /home/osint/app

# Add application files
WORKDIR /home/osint/app


# Customize shell with Zsh
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t https://github.com/denysdovhan/spaceship-prompt \
    -a 'SPACESHIP_PROMPT_ADD_NEWLINE="false"' \
    -a 'SPACESHIP_PROMPT_SEPARATE_LINE="false"' \
    -p git \
    -p ssh-agent \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions

COPY . .
RUN chown -R osint:osint /home/osint

# Supervisord configuration
COPY docker/supervisord.conf /etc/supervisord.conf

# Update database
RUN updatedb


# Entrypoint script
COPY start.sh /home/osint/start.sh
RUN chmod +x /home/osint/start.sh && chown osint:osint /home/osint/start.sh
#ENTRYPOINT ["/home/osint/start.sh"]


# Expose application port
EXPOSE 8003
EXPOSE 5001
# Start the supervisord
#CMD ["supervisord", "-c", "/etc/supervisord.conf"]

#cd /home/osint/app || exit 2
#uvicorn main:app --host 0.0.0.0 --port 8003 --reload

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]