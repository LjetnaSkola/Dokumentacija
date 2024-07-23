#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

uint32_t stringLength(const char str[]);
void stringTrim(char str[]);
uint8_t extractSubstring(const char inStr[], char outStr[],
                         uint_least32_t beginning, uint_least32_t end);
uint8_t concatStrings(char str1[], const char str2[]);

uint32_t stringLength(const char str[]) {
  uint32_t len = 0;
  while (str[len] != '\0') {
    len++;
  }
  return len;
}

void stringTrim(char str[]) {
  uint32_t lastChar;
  uint32_t count;
  uint32_t count2;
  uint32_t len = stringLength(str);
  char *newStr = (char *)malloc(sizeof(char) * stringLength(str) + 1);
  if (newStr == NULL) {
    printf("Error allocating memory.");
    return;
  }

  // find the first non-space character
  for (count = 0; str[count] == ' '; count++) {
  }

  printf("first char: %d\n", count);

  lastChar = count;

  // find the last non-space character
  for (count2 = count; str[count2] != '\0'; count2++) {
    lastChar = str[count2] == ' ' ? lastChar : count2;
  }
  printf("last char: %d\n", lastChar);

  //  put the new string into the new tmp string
  int i;
  for (i = 0; i + count <= lastChar; i++) {
    newStr[i] = str[i + count];
  }
  newStr[i] = '\0';

  // put it all back
  for (count = 0; newStr[count] != '\0'; count++) {
    str[count] = newStr[count];
  }
  str[count] = '\0';
}

uint8_t extractSubstring(const char inStr[], char outStr[],
                         uint_least32_t beginning, uint_least32_t end) {
  if (beginning < 0 || end > stringLength(inStr) - 1 || inStr == NULL ||
      outStr == NULL) {
    printf("Error extracting substring!\n");
    return 0;
  }
  int i;
  for (i = beginning; i <= end; i++) {
    outStr[i - beginning] = inStr[i];
  }
  if (outStr[i - beginning - 1] != '\0') {
    outStr[i - beginning] = '\0';
  }
  return 1;
}
uint8_t concatStrings(char str1[], const char str2[]) {
  uint32_t len = stringLength(str1) + stringLength(str2) + 1;
  uint32_t len1 = stringLength(str1);
  int i = 0;
  for (i = len1; i < len; i++) {
    str1[i] = str2[i - len1];
  }
  str1[i] = '\0';
  return 1;
}

int main() {
  char string[10] = "  he lo  ";
  printf("Len: %d\n", stringLength(string));
  stringTrim(string);
  printf("Trimmed: %s\n", string);

  char string2[20] = "danilo ";
  char string3[10];
  extractSubstring(string2, string3, 2, 7);
  printf("Substr: %s\n", string3);

  char string4[30] = "test ";
  char string5[5] = "no3";

  concatStrings(string4, string5);
  printf("Concatenated: %s\n", string4);
  return 0;
}
