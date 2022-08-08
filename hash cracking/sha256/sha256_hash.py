# Code written by https://github.com/Sajmonpcgamer
import hashlib

print("==============================\nmd5 hash creator\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer\n==============================\n")

h = str(input("Word to be hashed: ")).encode()
h = hashlib.md5(h).hexdigest()
print(f"Hash (Hex): {h}")
