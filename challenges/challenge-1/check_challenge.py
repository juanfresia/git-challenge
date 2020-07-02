#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")

print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."
assert repo.commit('master').tree.hexsha == "e58562979d51531c06ad23f3c196f34c94342ebc", "Wrong tree"

print("Passed!")

