CHALLENGE?=1
DOCKERFILE?="Dockerfile"

.DEFAULT: all
all: build

unpack:
	mv repo/git repo/.git
	mv repo/tree/* repo/
	rmdir repo/tree
.PHONY: unpack

pack:
	mv repo tree
	mkdir repo
	mv tree repo
	mv repo/tree/.git repo/git
.PHONY:pack

build:
	sudo docker build -t gitchallenge/challenge-$(CHALLENGE) -f $(DOCKERFILE) .
.PHONY: build

run: build
	sudo docker run --rm -it gitchallenge/challenge-$(CHALLENGE)
.PHONY: run

push: build
	sudo docker push gitchallenge/challenge-$(CHALLENGE)
.PHONY: push
