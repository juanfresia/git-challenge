#! /usr/bin/env python
"""
CLI tool to compute euclid algorithm, find gcd and
inverse mod N
"""

import argparse

def euclid(a, b, show=False):
    r0 = [a, 1, 0]
    r1 = [b, 0, 1]
    if show: print(r0)
    if show: print(r1)
    while r1[0] != 0:
        q = r0[0] // r1[0]
        rn = [x - q*y for x, y in zip(r0, r1)]

        r0 = r1
        r1 = rn
        if show: print(r1)

    return r0

def gcd(a, b):
    return euclid(a, b)[0]

def inverse(a, n):
    r = euclid(a, n)
    if r[0] == 1:
        return r[1]
    return 0

print("euclid(1759, 550)")
print(euclid(1759, 550, show=True))

print()
print("gcd(1759, 550) = ", gcd(1759, 550))

print()
print("inverse_550(1759) =", inverse(1759, 550))

if __name__ == "__main__":
    # Set arguments
    parser = argparse.ArgumentParser(description='Compute euclid algorithm')
    parser.add_argument('operation', help="Type of operation to perform", choices=['euclid', 'inverse', 'gcd'])
    parser.add_argument('numA', help='First number', nargs=1, type=int)
    parser.add_argument('numB', help='Second number', nargs=1, type=int)
    parser.add_argument('-s', '--show', help='Show full procedure', action='store_true')

    args = parser.parse_args()

    a = args.numA[0]
    b = args.numB[0]
    show = args.show

    if args.operation == "euclid":
        res = euclid(a, b, show)
    elif args.operation == "gcd":
        res = gcd(a, b)
    else:
        res = inverse(a, b)

    print(res)
