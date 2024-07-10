#include "stdio.h"
#include "stdlib.h"
#include "LinkedList.h"

void add(NODE **head, int value)
{
  NODE *new = (NODE *)malloc(sizeof(NODE));
  new->value = value;
  if (*head == NULL)
  {
    new->next = *head;
    *head = new;
  }
  else
  {
    NODE *p = (NODE *)malloc(sizeof(NODE));
    for (p = *head; p->next ;p = p->next);
        new->next = p->next;
    p->next = new;
  }
}
void print(NODE *head)
{
    while(head)
    {
        printf("%d\n", head->value);
        head=head->next;
    }
}
int delete1(NODE **head, int key)
{
    if (*head == 0)
        return 0;
    else
    {
        NODE *p;
        if ((*head)->value==key)
        {
            p = (*head);
            (*head) = (*head)->next;
        }
        else
        {
            NODE *pr = (*head);
            for (p = (*head)->next;p;p = p->next)
                pr = p;
            if (p == 0)
                return 0;
            pr->next = p->next;
        }
        free(p);
        return 1;
    }
    return 0;
  
}