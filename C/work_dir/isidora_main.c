/*
 * main.c
 *
 *  Created on: Jul 10, 2024
 *      Author: student
 */

#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int data;
	struct Node *next;
} Node;

void printLinkedlist(Node* p);
void addElementAfter(Node* prev_node, int new_data);
void addElementToTheBeginning(Node** head);
void addElementToTheEnd(Node* head);
void deleteNode(Node** head);
int searchElementByValue(Node* head);

int main(void) {
	Node *head;

	Node *element1;
	Node *element2;
	Node *element3;

	element1 = malloc(sizeof(Node));
	element2 = malloc(sizeof(Node));
	element3 = malloc(sizeof(Node));

	// Assign the values to the nodes
	element1->data = 10;
	element2->data = 20;
	element3->data = 30;

	// Link the elements
	element1->next = element2;
	element2->next = element3;
	element3->next = NULL;

	head = element1;
	printLinkedlist(head);

	addElementAfter(head->next, 5);
	printLinkedlist(head);

	deleteNode(&head);
	printLinkedlist(head);

	addElementToTheBeginning(&head);
	printLinkedlist(head);

	addElementToTheEnd(head);
	printLinkedlist(head);

	searchElementByValue(head);

	return 0;
}

void printLinkedlist(Node* p) {
	while (p != NULL) {
		printf("%d ", p->data);
		p = p->next;
	}
	printf("\n");
}

void addElementAfter(Node* prev_node, int new_data) {
  if (prev_node == NULL) {
  printf("the given previous node cannot be NULL");
  return;
  }

  Node* new_node = malloc(sizeof(Node));
  new_node->data = new_data;
  new_node->next = prev_node->next;
  prev_node->next = new_node;
}

void addElementToTheBeginning(Node** head) {
	int newData;
	Node *newNode;

	printf("Enter the value to be added to the singly linked list: ");
	scanf("%d", &newData);

	newNode = malloc(sizeof(Node));
	newNode->data = newData;
	newNode->next = (*head);
	*head = newNode;
}

void addElementToTheEnd(Node* head) {
	int newData;
	Node *newNode;

	printf("Enter the value to be added to the singly linked list: ");
	scanf("%d", &newData);

	newNode = malloc(sizeof(Node));
	newNode->data = newData;
	newNode->next = NULL;

	while (head->next != NULL) {
		head = head->next;
	}

	head -> next = newNode;
}

void deleteNode(Node** head) {
	int inputValue;
	Node* temp = *head;
	Node* prev;

	printf("Enter the value which you wish to delete from the singly linked list: ");
	scanf("%d", &inputValue);


		if (temp != NULL && temp->data == inputValue) {
		  *head = temp->next;
		  free(temp);
		  return;
		}

		while (temp != NULL && temp->data != inputValue) {
		  prev = temp;
		  temp = temp->next;
		}

		  // If the key is not present
		  if (temp == NULL) return;

		  // Remove the node
		  prev->next = temp->next;

		  free(temp);

}

int searchElementByValue(Node* head) {
	int inputValue;

	printf("Enter the value which you wish to search for in the singly linked list: ");
	scanf("%d", &inputValue);

	while (head->next != NULL) {
		if(head -> data == inputValue) {
			printf("Such value exists in this linked list!");
			return 1;
		} else
			head = head->next;
	}
	printf("Such value doesn't exist in this linked list!");
	return 0;
}
