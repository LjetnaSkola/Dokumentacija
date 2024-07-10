#include <stdio.h>
#include "linked_list.h"

/* finding the specified node of a linked list */
struct Node* find(struct Node** head, int data){

	if (head == NULL) return NULL;
	struct Node* temp = *head;
	while(temp!=NULL && temp->data!=data){
		temp = temp->next;
	}
	return temp;
}

/* delete a specific node of a linked list  */
int delete_data(struct Node** head, int data){

	struct Node* temp = find(head, data);

	if (temp == NULL) return -1;	// no such data
	if (*head == temp){				// deleting head (from the beginning)
		delete_from_beggining(head);
		return 1;
	}
	if (temp->next == NULL){		// deleting from the end
		delete_from_end(head);
		return 1;
	}
	/*delete from the middle*/
	temp->prev->next = temp->next;
	temp->next->prev = temp->prev;
	free(temp);
	return 1;
}

/* delete a node at the end of a linked list  */
int delete_from_end(struct Node** head){

	if (head == NULL) return -1;
	struct Node* temp = *head;
	while(temp->next!=NULL){
		temp = temp->next;
	}
	if (*head != temp){				// not a single element list
		temp->prev->next = NULL;
		free(temp);
		return 1;
	}
	// a single element list
	*head = NULL;
	free(temp);
	return 1;
}

/* delete a node at the beginning of a linked list  */
int delete_from_beggining(struct Node** head){

	if (head == NULL) return -1;
	struct Node* temp = *head;
	if ((*head)->next == NULL){		// a single element list
		free(*head);
		*head = NULL;
		return 1;
	}
	(*head)->next->prev = NULL;
	*head = temp->next;
	free(temp);
	return 1;
}

/* Function to create a new node */
struct Node* createNode(int data) {

    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

/*  insert a new node at the beginning of a linked list */
int insert_at_beggining(struct Node** head, int data){

	if (head == NULL) return -1;

	struct Node* newNode = createNode(data);
	newNode->next = *head;
	(*head)->prev = newNode;
	*head = newNode;
	return 1;
}

/*  insert a new node at the end of a linked list */
int insert_at_end(struct Node** head, int data){

	if (head == NULL) return -1;
	struct Node* temp = *head;
	while(temp->next!=NULL){
		temp = temp->next;
	}
	struct Node* newNode = createNode(data);
	temp->next = newNode;
	newNode->prev = temp;
	return 1;
}

/*  insert a new node after specified node of a linked list */
int insert_after(struct Node** head, int after, int data){

	if (head == NULL) return -1;

	struct Node* afterNode = find(head, after);
	struct Node* newNode = createNode(data);
	newNode->prev = afterNode;
	newNode->next = afterNode->next;
	afterNode->next->prev = newNode;
	afterNode->next = newNode;
	return 1;
}

/*  insert a new node before specified node of a linked list */
int insert_before(struct Node** head, int before, int data){

	if (head == NULL) return -1;

	struct Node* beforeNode = find(head, before);
	struct Node* newNode = createNode(data);
	newNode->prev = beforeNode->prev;
	newNode->next = beforeNode;
	beforeNode->prev->next = newNode;
	beforeNode->prev = newNode;
	return 1;
}
