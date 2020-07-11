#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")


print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').tree.hexsha == "a057730f0c670858ee3e5515cbf88972d7b44bc1", "Wrong tree"
assert repo.commit('master~1').hexsha == "eaff07ddaf2acf046f0d9432d2ec2edd0d276cdb", "Wrong commit"
assert repo.commit('master~1').tree.hexsha == "50cfbbc27bd13be7de55c61a22dcab458445f294", "Wrong commit"

print("Passed!")

