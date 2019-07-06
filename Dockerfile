FROM ubuntu:18.04

RUN apt-get update && apt-get install -y git vim git-completion bash-completion
RUN apt-get install -y python3 python3-pip
RUN pip3 install gitpython

COPY .gitconfig /root/.gitconfig

WORKDIR /challenge
COPY README.md README.md

COPY remote     .remote
COPY repo/git   repo/.git
COPY repo/tree  repo

COPY check_challenge.py /usr/local/sbin/check_challenge

RUN echo "source /usr/share/bash-completion/completions/git" >> /root/.bashrc

ENTRYPOINT ["/bin/bash"]
