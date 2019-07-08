#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")


print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').tree.hexsha == "adea2e5f4c6ac11a25c59a18bf3527f7c4be0445", "Wrong tree"
assert repo.commit('master^1').hexsha == "bc255866b36b696f8f465432793d1d5bd6b48267", "Wrong commit"
assert repo.commit('master^1').tree.hexsha == "a057730f0c670858ee3e5515cbf88972d7b44bc1", "Wrong commit"

print("Passed!")

