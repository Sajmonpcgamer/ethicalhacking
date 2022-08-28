import string
import sys
import itertools

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
cha = list(itertools.permutations(list(allchars), amount))

for i in cha:
	w += "".join(map(str, i))
	w += "\n"

with open("list.txt", "w") as f:
	f.write(w)
