CHALLENGE?=1
DOCKERFILE?="Dockerfile"

.DEFAULT: all
all: build

build:
	sudo docker build -t challenge-$(CHALLENGE) -f $(DOCKERFILE) .
.PHONY: build

run: build
	sudo docker run --rm -it challenge-$(CHALLENGE)
.PHONY: run
