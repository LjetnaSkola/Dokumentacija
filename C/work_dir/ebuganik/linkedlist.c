/*
 * linkedlist.c
 *
 *  Created on: Jul 10, 2024
 *      Author: Emanuela Buganik
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct Node{
	int data;
	struct Node* next;
};

void addAtBeggining(struct Node** head, int value)
{
	struct Node* node = (struct Node*)malloc(sizeof(struct Node));
	node->data = value;
	node->next = *head;
	*head = node;
}


void addAtEnd(struct Node** head, int value)
{
	struct Node* node = (struct Node*)malloc(sizeof(struct Node));
	node->data = value;
	node->next = NULL;

	/* Check if this is the first node, linked list is empty */

	if(*head == NULL)
		{*head = node;
		return;}

	/* Traverse through all nodes in linked list*/
	struct Node* tmp = *head;
	while(tmp->next != NULL)
	{
		tmp = tmp->next;
	}
	tmp->next = node;

}

void printLinkedList(struct Node* head)
{
	struct Node* tmp = head;
	while(tmp!= NULL)
	{
		printf("%d ", tmp->data);
	}
}

bool searchByKey(struct Node* head, int key)
{
	struct Node* tmp = head;
	while(tmp != NULL)
	{
		if(tmp->data == key)
			return true;
		tmp = tmp->next;
	}
	return false;
}

void deleteNodeByKey(struct Node** head, int key)
{
	struct Node* tmp = *head, *prev;
	/* In case if its head node that has the key*/
	if(tmp != NULL && tmp->data == key)
	{
		*head = tmp->next;
		free(tmp);
		return;
	}
	if(tmp != NULL && tmp->data != key)
	{
		prev = tmp;
		tmp = tmp->next;
	}

	/* No key found */
	if(tmp == NULL)
		return;

	prev->next = tmp->next;
	free(tmp);

}
void deleteLinkedList(struct Node** head)
{
  
   struct Node* tmp = *head;
   struct Node* next;
 
   while (tmp != NULL) 
   {
       next = tmp->next;
       free(tmp);
       tmp = next;
   }

   *head = NULL;
}

int main()
{
	/* Head pointer of linked list */
	struct Node* head = NULL;
	int key = 25;
	/* Adding nodes in linked list at the begging and at the end */
	addAtBeggining(&head, 10);
	addAtEnd(&head, 7);
	addAtEnd(&head, 20);
	addAtEnd(&head, 24);

	/* Print linked list content */
	printf("Linked list data :");
	printLinkedList(head);

	/* Check whether integer data(key) could be found in linked list */
	if(searchByKey(head,key))
	{
		printf("Key %d found in linked list!", key);
	}
	else printf("Key %d couldn't be found in linked list!", key);

	deleteNodeByKey(&head, 10);
	printf("Linked list after deletion: ");
	printLinkedList(head);
	/* Free linked list */
	delete(&head);
	return 0;


}
