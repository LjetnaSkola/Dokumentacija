#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdio.h>
#include <inttypes.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>

#define max_num 20

/* NODE struct */
typedef struct node 
{
	int_least32_t id;
	char name[max_num];
	struct node* next;
} NODE;

/*Adds node at the beinning of a list. */
int_least32_t addFront (NODE** head, int_least32_t id_param, char* name_param)
{
	NODE* new_node = (NODE*)malloc(sizeof(NODE));
	new_node -> id = id_param;
	new_node -> next = NULL;
	strncpy(new_node->name, name_param, max_num);
	if(new_node == NULL)
	{
		return -1;
	}
	new_node -> next = *head;
	*head = new_node;
	return 0;
}

/*Adds node after the given node in a list. */
int_least32_t addMiddle (NODE** current, int_least32_t id_param, char* name_param)
{
	NODE* new_node = (NODE*)malloc(sizeof(NODE));
	new_node -> id = id_param;
	new_node -> next = NULL;
	strncpy(new_node->name, name_param, max_num);
	if(new_node == NULL)
	{
		return -1;
	}
	NODE* next_node = (*current)->next;
	(*current)->next = new_node;
	new_node -> next = next_node;
	return 0;
}

/*Adds node at the end of a list. */
int_least32_t addRear (NODE** head, int_least32_t id_param, char* name_param)
{
	NODE* new_node = (NODE*)malloc(sizeof(NODE));
	new_node -> id = id_param;
	new_node -> next = NULL;
	strncpy(new_node->name, name_param, max_num);
	if(new_node == NULL)
	{
		return -1;
	}
	
	NODE* p = *head;
	for(p; p -> next != NULL; )
	{
		p = p -> next;
	}
	p -> next = new_node;
	return 0;
}

int_least32_t findById (NODE** head, int_least32_t id_param)
{
	NODE* p = *head;
	for( p ; p -> id != id_param; )
	{
		if(p -> id == id_param)
		{
			return id_param;
		}
		p = p -> next;
	}
	return -1;
}

int_least32_t deleteByIdAndName(NODE** head, int_least32_t id_param, char* name_param)
{
	NODE* current = *head;
	NODE* previous = NULL;
	
	
	for(; current->id != id_param && !(strcmp(current->name, name_param)); current = current->next)
	{
		previous = current;
		current = current -> next;
	}
	if(current == NULL)
	{
		return -1;
	}
	if(previous == NULL)
	{
		*head = current -> next;
		return 0;
	}
	else
	{
		previous -> next = current -> next;
		free(current);
		current = NULL;
		return 0;
	}
	
}

void printList (NODE* head)
{
	NODE* current = head;
    while (current != NULL) 
	{
        printf("ID: %ld, Name: %s\n", current->id, current->name);
        current = current->next;
    }
    printf("\n");
}
void freeList(NODE* head)
{
	NODE* current = head;
    while (current != NULL) 
	{
        NODE* temp = current;
        current = current->next;
        free(temp);
    }
}
/*
void sortByIdAscending(NODE **headRef) {
    int swapped;
    NODE *ptr;
    NODE *lptr = NULL;

    if (*headRef == NULL) {
        printf("Empty list\n");
        return;
    }

    do {
        swapped = 0;
        ptr = *headRef;

        while (ptr->next != lptr) {
            if (ptr->id > ptr->next->id) {
                NODE *temp = swap(ptr, ptr->next);
                swapped = 1;

               
                if (temp == *headRef)
                    *headRef = temp;
            }
            else {
                ptr = ptr->next;
            }
        }
        lptr = ptr; 
    } while (swapped);
}

NODE* swap(NODE* ptr1, NODE* ptr2) {
    NODE* tmp = ptr2->next;
    ptr2->next = ptr1;
    ptr1->next = tmp;
    return ptr2;
}
*/

#endif