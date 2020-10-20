#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")

print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."
assert repo.commit('master').tree.hexsha == "bb5d4918427030bb9e707ddf80f74d8f8de830aa", "Wrong tree"
assert repo.commit('master^1').hexsha == "0f5220c5b02d5a8a5eee55ae38bf82a8eff23e9b", "Wrong commit"

print("Passed!")

