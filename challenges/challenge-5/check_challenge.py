#! /usr/bin/python3

from git import Repo

repo = Repo("/challenge/.remote")


print("Checking level...")

assert repo.bare, "Oops! Remote is not a bare repository."

assert repo.commit('master').tree.hexsha == "8c197b3ece25a5e1dfadd18c0e7a7456a643fde5", "Wrong tree"
assert repo.commit('master~1').tree.hexsha == "8c197b3ece25a5e1dfadd18c0e7a7456a643fde5", "Wrong tree"
assert repo.commit('master~2').tree.hexsha == "e9786a6fff13993c8fa61454a3dadbf74e18d280", "Wrong tree"
assert repo.commit('master~3').tree.hexsha == "bb5f4cf565eafa735b8db5ccf220d302c0b00653", "Wrong tree"

print("Passed!")

