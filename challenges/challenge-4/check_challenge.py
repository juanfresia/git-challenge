#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")


print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').tree.hexsha == "b70e985a104f8901f898c66b518b8b2d03e34d6d", "Wrong tree"
assert repo.commit('master~1').tree.hexsha == "65571b1bf1e8f2d061610cbad2f1645d10fe4c90", "Wrong tree"
assert repo.commit('master~2').hexsha == "d1e8616868cf696afc8109f4e59a8be25eeb25a1", "Wrong commit"
assert repo.commit('master~2').tree.hexsha == "b39c228897e315823321ce22c597f15d0cdbaada", "Wrong tree"

print("Passed!")

