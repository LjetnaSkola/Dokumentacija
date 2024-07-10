/*
 * main.c
 *
 *  Created on: Jul 10, 2024
 *      Author: student
 */
#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
	int node_data;
	struct Node *node_ptr;
} Node;

Node* create_node(int data) {
	Node *new_node = (Node*) malloc(sizeof(Node));
	if (new_node == NULL) {
		printf("New node is NULL!");
		exit(1);
	}
	new_node->node_data = data;
	new_node->node_ptr = NULL;

	return new_node;
}

void add_at_head(Node **head, int data) {
	Node *node = create_node(data);
	node->node_ptr = *head;
	*head = node;

	printf("Added %d at head\n", data);
}

void delete_at_head(Node **head) {
	if (*head == NULL) {
		printf("Empty list!");
		return;
	}
	Node *node = *head;
	*head = (*head)->node_ptr;
	printf("Deleted %d at head\n", node->node_data);
	free(node);

}

void add_at_tail(Node **head, int data) {
	Node *node = create_node(data);

	if (*head == NULL) {
		*head = node;
		return;
	}

	Node *current = *head;
	while (current->node_ptr != NULL) {
		current = current->node_ptr;
	}

	current->node_ptr = node;
	node->node_ptr = NULL;

	printf("Added %d at tail\n", data);
}

void delete_at_tail(Node **head) {
	if (*head == NULL) {
		printf("Empty list!");
		return;
	}
	if ((*head)->node_ptr == NULL) { //ako imamo jedan element
		free(*head);
		*head = NULL;
		return;
	}
	Node *node = *head;
	while (node->node_ptr->node_ptr != NULL) {
		node = node->node_ptr;
	}
	printf("Deleted %d at tail\n", node->node_ptr->node_data);
	free(node->node_ptr);
	node->node_ptr = NULL;
}

void add_at_index(Node **head, int index, int data) {
	if (index < 0) {
		printf("Negative index!");
		return;
	}

	Node *node = create_node(data);
	if (index == 0) {
		node->node_ptr = *head;
		*head = node;
		return;
	}

	Node *current = *head;

	for (int i = 0; i < index - 1; i++) {
		if (current == NULL) {
			printf("Index out of bounds.\n");
			free(node);
			return;
		}
		current = current->node_ptr;
	}
	node->node_ptr = current->node_ptr;
	current->node_ptr = node;

	printf("Added %d at %d positin\n", data, index);
}

void delete_at_index(Node **head, int index) {
	if (index < 0) {
		printf("Negative index!");
		return;
	} else if (*head == NULL) {
		printf("List error!");
		return;
	}
	if (index == 0) {
		delete_at_head(head);
		return;
	}

	Node *current = *head;
	for (int i = 0; i < index - 1; i++) {
		if (current == NULL || current->node_ptr == NULL) {
			printf("Index out of bounds.\n");
			return;
		}
		current = current->node_ptr;
	}
	Node *node = current->node_ptr;
	current->node_ptr = node->node_ptr;
	printf("Deleted %d at %d position\n", node->node_data, index);
	free(node);

}

void search_by_data(Node **head, int data){
	Node *node = *head;
	int i=0;
	while(node!=NULL){
		if(node->node_data == data){
			printf("Data %d found at %d position\n", data,i );
			return;
		}
		i++;
		node=node->node_ptr;

	}
	printf("Data %d not found\n", data);
}

void print_list(Node *head) {
	Node *current = head;
	while (current != NULL) {
		printf("%d ", current->node_data);
		current = current->node_ptr;

		if (current != NULL) {
			printf("--> ");
		} else {
			printf("\n");
		}
	}
	printf("\n");
}

int main() {

	Node *head = NULL;
	add_at_head(&head, 4);
	print_list(head);
	add_at_head(&head, 8);
	add_at_tail(&head, 6);
	add_at_index(&head, 2, 10);

	print_list(head);

	add_at_index(&head, 7, 8);
	add_at_index(&head, 4, 8);
	add_at_tail(&head, 34);
	add_at_tail(&head, 94);

	print_list(head);

	delete_at_head(&head);
	delete_at_tail(&head);

	print_list(head);
	search_by_data(&head, 8);
	search_by_data(&head, 124);

	delete_at_index(&head, 0);
	delete_at_index(&head, 2);
	delete_at_tail(&head);

	print_list(head);

	printf("Press Enter to exit...");
	getchar();

	return 0;
}
