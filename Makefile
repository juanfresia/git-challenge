CHALLENGE?=1
DOCKERFILE?="Dockerfile"

.DEFAULT: all
all: build

# Separate git repository and working tree into
# different directories, because git gets confused when
# working with nested repositories in a no-submodules fashion.
pack: repo/.git
	mv repo tree
	mkdir repo
	mv tree repo
	mv repo/tree/.git repo/git
.PHONY:pack

# Revert the packing operation
unpack: repo/git
	mv repo/git repo/.git
	mv repo/tree/* repo/
	rmdir repo/tree
.PHONY: unpack

## Targets to work with docker images
build:
	sudo docker build -t gitchallenge/challenge-$(CHALLENGE) -f $(DOCKERFILE) .
.PHONY: build

run: build
	sudo docker run --rm -it gitchallenge/challenge-$(CHALLENGE)
.PHONY: run

push: build
	sudo docker push gitchallenge/challenge-$(CHALLENGE)
.PHONY: push
