#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")

print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').hexsha == "9a010cc325b4619756f284cf27d0b2fa19e30ff8", "Wrong commit"

print("Passed!")

