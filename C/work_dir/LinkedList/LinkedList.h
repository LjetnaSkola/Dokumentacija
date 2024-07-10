#include "stdio.h"
#include "stdlib.h"

typedef struct LinkedList
{
    int value;
    struct LinkedList *next;
}NODE;

void add(NODE **head, int value);
void print(NODE *head);
void delete1(NODE **head, int key);
