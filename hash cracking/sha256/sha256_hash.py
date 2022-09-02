# Code written by https://github.com/Sajmonpcgamer
import hashlib
import sys

h = hashlib.sha256(sys.argv[1].encode()).hexdigest()
print(h)