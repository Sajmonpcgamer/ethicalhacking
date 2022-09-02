# Code written by https://github.com/Sajmonpcgamer

import os.path
import hashlib
import string
import random
from os import getcwd
from sys import argv as args
from sys import platform as SYSPLAT
import math
millnames = ['','k','M','B','T','Q','Qu','S']
def millify(n:float):
	millidx = max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
	return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

print("=" * 50)
print("MD5 Hash Cracker\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer")
print("=" * 50)
print()

if "--random" in str(args) or "-r" in args:
	if len(args) < 3:
		exit("Hash and max length needs to be specified")
	elif args[1] == "--random" or args[2] == "--random":
		exit("python3 md5_hash_cracker.py <hash> <max_length> --random")
	h = args[1].encode()
	m_l = int(args[2])
	h_t = None
	h_c = string.ascii_letters + string.digits + string.punctuation + string.whitespace

	print("==============================\nmd5 hash cracker\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer\n==============================\n")
	print("!Warning this is a BETA feature, only hex works!")

	while h_t != h:
		h_t = hashlib.md5(str(random.choice(h_c) for i in range(random.randint(1, m_l))).encode()).hexdigest().encode()
	exit("Hash cracked!\nCracked hash: " + h_t)
else:
	if len(args) < 3:
		exit("python3 md5_hash_cracker.py <list> <hash>\nOptions:\n\t--hex = enables HEX mode\n\t--random = uses random strings")
	filename = args[1]
	if not "/" in filename or not "\\" in filename:
		if "win" in SYSPLAT:
			filename = getcwd() + "\\" + str(args[1])
		else:
			filename = getcwd() + "/" + str(args[1])
	if not os.path.exists(filename):
		exit("This list does not exist!")
	if not os.path.isfile(filename):
		exit("This is not a file!")
	print("==============================\nmd5 hash cracker\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer\n==============================\n")

	h = args[2].encode()

	if "--hex" in str(args) or "-h" in str(args):
		print("Hex Mode enabled!")

	words = []
	with open(filename, "r") as l:
		words = l.readlines()
		l.close()

	index = 0
	l = millify(len(words))
	for i in words:
		w = hashlib.md5(i.replace("\n", "").encode())
		if "--hex" in str(args) or "-h" in str(args):
			w = w.hexdigest().encode()
		else:
			w = w.digest()
		index += 1
		print(f"\rTried: {millify(index)}/{l}      ", end="")
		if w == h:
			print("\n")
			print("=" * 50)
			exit("Hash cracked!\nCracked hash: " + i + ("=" * 50))
	exit("\nHash was not found :(")
exit()
