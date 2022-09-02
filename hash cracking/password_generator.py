import string
import random
import sys

amount = int(sys.argv[1])

allchars = ""

if "--lower" in str(sys.argv): allchars += string.ascii_lowercase
if "--upper" in str(sys.argv): allchars += string.ascii_uppercase
if "--all" in str(sys.argv): allchars += (string.ascii_letters + string.digits + string.punctuation)
if "--letters" in str(sys.argv): allchars += string.ascii_letters
if "--digits" in str(sys.argv): allchars += string.digits
if "--numbers" in str(sys.argv): allchars += string.digits
if "--special" in str(sys.argv): allchars += string.punctuation

pw = "".join(random.choice(allchars) for i in range(amount))
print(pw)