#ifndef LINKED_LIST_H
#define LINKED_LIST_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

enum
{
    MAX_NAME = 30
};

typedef struct LinkedListNode
{
    long id;
    char *name;
    struct LinkedListNode *next;
} LINKED_LIST_NODE;

typedef struct LinkedList
{
    LINKED_LIST_NODE *HEAD;
    LINKED_LIST_NODE *TAIL;
} LINKED_LIST;

void printList(LINKED_LIST *list);

int addTail(LINKED_LIST *const list, LINKED_LIST_NODE *const node);
int addHead(LINKED_LIST *const list, LINKED_LIST_NODE *const node);
int addNext(LINKED_LIST *const list, LINKED_LIST_NODE *const existingNode, LINKED_LIST_NODE *const newNode);

int removeNode(LINKED_LIST *list, const long id);

LINKED_LIST_NODE *findByName(LINKED_LIST *list, const char *const name);
LINKED_LIST_NODE *findById(LINKED_LIST *list, const long id);

#endif // LINKED_LIST_H