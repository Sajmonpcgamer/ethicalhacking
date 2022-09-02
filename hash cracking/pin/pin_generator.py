import sys
import math

if len(sys.argv) < 2: exit("Maximal value needs to be specified in arguments!")

millnames = ['','k','M','B','T','Q','Qu','S']
def millify(n:int):
    n = float(n)
    millidx = max(0,min(len(millnames)-1,int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))
    return '{:.0f}{}'.format(n / 10**(3 * millidx), millnames[millidx])

print("=" * 50)
print("PIN Code Generator\nWritten by Sajmonpcgamer\nhttps://github.com/Sajmonpcgamer")
print("=" * 50)
print()

max_val = int(sys.argv[1])

print("Maximal value set to: " + millify(max_val))

w = ""
print("Generating PIN Codes...")
l = millify(max_val)
for i in range(max_val+1):
	print(f"\rGenerated: {millify(i)}/{l}     ", end="")
	w += str(i)
	w += "\n"

print("\nWriting...")
with open("list.txt", "w") as f:
	f.write(w)
	f.close()
print("Done!")