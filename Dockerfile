FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git vim git-completion bash-completion

COPY .gitconfig /root/.gitconfig

WORKDIR /challenge
COPY README.md README.md

COPY remote     .remote
COPY repo/git   repo/.git
COPY repo/tree  repo

COPY check_challenge /usr/local/sbin

RUN echo "source /usr/share/bash-completion/completions/git" >> /root/.bashrc

ENTRYPOINT ["/bin/bash"]
