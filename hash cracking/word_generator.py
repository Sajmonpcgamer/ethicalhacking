import string
import sys
import itertools
import math
millnames = ['','k','M','B','T','Q','Qu','S']
def millify(n:int):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

def all_comb(l:list, length:int):
	ret = []
	for perm in itertools.permutations(l, length):
		ret.append("".join(perm))
	return ret

print("=" * 50)
print("Word Generator\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer")
print("=" * 50)
print()

amount = int(sys.argv[1])
allchars = ""

if "--lower" in str(sys.argv): allchars += string.ascii_lowercase
if "--upper" in str(sys.argv): allchars += string.ascii_uppercase
if "--all" in str(sys.argv): allchars += (string.ascii_letters + string.digits + string.punctuation)
if "--letters" in str(sys.argv): allchars += string.ascii_letters
if "--digits" in str(sys.argv): allchars += string.digits
if "--numbers" in str(sys.argv): allchars += string.digits
if "--special" in str(sys.argv): allchars += string.punctuation

print(f"'{allchars}'")

w = str("")
print("Generating list...")
cha = all_comb(list(allchars), amount)

print("Converting to string...")
index = 0
l = millify(len(cha))
for i in cha:
	print(f"\rConverted: {millify(index)}/{l}     ", end="")
	w += "".join(map(str, i))
	w += "\n"
	index += 1

print("\nWriting...")
with open("list.txt", "w") as f:
	f.write(w)
	f.close()
print("Done!")