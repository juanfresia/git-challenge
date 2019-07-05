FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git vim

COPY .gitconfig /root/.gitconfig

WORKDIR /challenge
COPY README.md README.md

COPY remote /challenge/.remote
COPY repo   /challenge/repo

COPY check_challenge /usr/local/sbin

ENTRYPOINT ["/bin/bash"]
