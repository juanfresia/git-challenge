#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")

print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').hexsha == "a6778fe48ba5f923fe26dee3052699f85d965af2", "Wrong commit"

print("Passed!")

