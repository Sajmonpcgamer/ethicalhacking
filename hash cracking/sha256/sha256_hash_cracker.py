# Code written by https://github.com/Sajmonpcgamer

import os.path
import hashlib
import string
import random
from os import getcwd
from sys import argv as args
from sys import platform as SYSPLAT

if "--random" in str(args) or "-r" in args:
    if len(args) < 3:
        exit("Hash and max length needs to be specified")
    elif args[1] == "--random" or args[2] == "--random":
        exit("python3 sha256_hash_cracker.py <hash> <max_length> --random")
    h = args[1].encode()
    m_l = int(args[2])
    h_t = None
    h_c = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    print("==============================\nsha256 hash cracker\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer\n==============================\n")
    print("!Warning this is a BETA feature, only hex works!")

    while h_t != h:
        h_t = hashlib.sha256(str(random.choice(h_c) for i in range(random.randint(1, m_l))).encode()).hexdigest().encode()
    exit("Hash cracked!\nCracked hash: " + h_t)
else:
    if len(args) < 3:
        exit("python3 sha256_hash_cracker.py <list> <hash>\nOptions:\n\t--hex = enables HEX mode\n\t--random uses random strings")
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

    print("==============================\nsha256 hash cracker\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer\n==============================\n")

    h = args[2].encode()

    if "--hex" in str(args) or "-h" in str(args):
        print("Hex Mode enabled!")

    words = []
    with open(filename, "r") as l:
        words = l.readlines()

    for i in words:
        w = hashlib.sha256(i.replace("\n", "").encode())
        if "--hex" in str(args) or "-h" in str(args):
            w = w.hexdigest().encode()
        else:
            w = w.digest()
        
        if w == h:
            exit("Hash cracked!\nCracked hash: " + i)

    exit("Hash was not found :(")
exit()
