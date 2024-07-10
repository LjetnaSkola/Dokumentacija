#include "linked-list.h"

void printList(LINKED_LIST *list)
{
    LINKED_LIST_NODE *iterator = list->HEAD;
    for (int i = 0; iterator != NULL; iterator = iterator->next, i++)
    {
        printf("#%d) {id: %ld, name: %s}\n", i, iterator->id, iterator->name);
    }
}

int addTail(LINKED_LIST *const list, LINKED_LIST_NODE *const node)
{
    if (list->HEAD != NULL)
    {
        node->next = list->TAIL->next;
        list->TAIL->next = node;
        list->TAIL = node;
        return 1;
    }

    list->HEAD = node;
    list->TAIL = node;
    return 1;
}

int addHead(LINKED_LIST *const list, LINKED_LIST_NODE *const node)
{
    if (list->HEAD != NULL)
    {
        node->next = list->HEAD->next;
        list->HEAD->next = node;
        list->HEAD = node;
        return 1;
    }

    list->HEAD = node;
    list->TAIL = node;
    return 1;
}

int addNext(LINKED_LIST *list, LINKED_LIST_NODE *const existingNode, LINKED_LIST_NODE *const newNode)
{
    if (existingNode->next == NULL)
    {
        return addTail(list, newNode);
    }
    newNode->next = existingNode->next;
    existingNode->next = newNode;
    return 1;
}

int removeNode(LINKED_LIST *list, const long id)
{
    if (list->HEAD->id == id)
    {
        list->HEAD = list->HEAD->next;
        if (list->HEAD == NULL)
        {
            list->TAIL = NULL;
        }
        return 1;
    }

    LINKED_LIST_NODE *iterator = list->HEAD;
    for (; iterator != NULL && iterator->next != NULL && iterator->next->id != id; iterator = iterator->next)
    {
    }
    if (iterator != NULL && iterator->next != NULL)
    {
        if (iterator->next != list->TAIL)
        {
            iterator->next = iterator->next->next;
            return 1;
        }
        list->TAIL = iterator;
    }
    return 0;
}

LINKED_LIST_NODE *findByName(LINKED_LIST *list, const char *const name)
{
    LINKED_LIST_NODE *iterator = list->HEAD;
    for (; iterator != NULL && strncmp(iterator->name, name, MAX_NAME) != 0; iterator = iterator->next)
    {
    }
    if (iterator != NULL)
    {
        return iterator;
    }
    return NULL;
}

LINKED_LIST_NODE *findById(LINKED_LIST *list, const long id)
{
    LINKED_LIST_NODE *iterator = list->HEAD;
    for (; iterator != NULL && iterator->id != id; iterator = iterator->next)
    {
    }
    if (iterator != NULL)
    {
        return iterator;
    }
    return NULL;
}