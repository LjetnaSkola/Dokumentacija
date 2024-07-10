#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Element {
    int id;
    char name[50];
    struct Element *next;
};

void printList(struct Element *head);
void addElement(struct Element **head, int id, const char *name);
void addElementAtIndex(struct Element **head, int index, int id, const char *name);
void deleteElement(struct Element **head, int id);
void freeList(struct Element **head);

int main() {
    struct Element *head = NULL;

    // Initialize the list with the first element
    head = (struct Element *) malloc(sizeof(struct Element));
    if (head == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    head->id = 100;
    strcpy(head->name, "Initial element");
    head->next = NULL;

    // Print the initial list
    printf("Initial List:\n");
    printList(head);
    printf("\n");

    // Add new elements
    addElement(&head, 105, "Second element");
    addElement(&head, 111, "Third element");
    addElementAtIndex(&head, 2, 120, "Fourth element at index 2");
    addElement(&head, 115, "Fifth element");

    // Print the updated list
    printf("List after adding elements:\n");
    printList(head);
    printf("\n");

    // Delete an element
    deleteElement(&head, 105);

    // Print the list after deletion
    printf("List after deleting element with id 105:\n");
    printList(head);
    printf("\n");

    // Free allocated memory
    freeList(&head);

    return 0;
}

void printList(struct Element *head) {
    struct Element *current = head;

    while (current != NULL) {
        printf("ID: %d, Name: %s\n", current->id, current->name);
        current = current->next;
    }
}

void addElement(struct Element **head, int id, const char *name) {
    struct Element *newElement = (struct Element *) malloc(sizeof(struct Element));
    if (newElement == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    newElement->id = id;
    strcpy(newElement->name, name);

    struct Element *current = *head;
    while(current->next != NULL){
    	current=current->next;
    }

    current->next=newElement;
    newElement->next = NULL;
}

void addElementAtIndex(struct Element **head, int index, int id, const char *name) {
    struct Element *newElement = (struct Element *) malloc(sizeof(struct Element));
    if (newElement == NULL) {
        printf("Memory allocation failed.\n");
        return;
    }

    newElement->id = id;
    strcpy(newElement->name, name);

    if (index == 0) {
        newElement->next = *head;
        *head = newElement;
        return;
    }

    struct Element *current = *head;
    for (int i = 0; i < index - 1 && current != NULL; i++) {
        current = current->next;
    }

    if (current == NULL) {
        printf("Index out of bounds. Adding element failed.\n");
        free(newElement);
        return;
    }

    newElement->next = current->next;
    current->next = newElement;
}

void deleteElement(struct Element **head, int id) {
    struct Element *current = *head;
    struct Element *prev = NULL;

    while (current != NULL && current->id != id) {
        prev = current;
        current = current->next;
    }

    if (current == NULL) {
        printf("Element with ID %d not found in the list.\n", id);
        return;
    }

    if (prev == NULL) {
        *head = current->next;
    } else {
        prev->next = current->next;
    }

    free(current);
}

void freeList(struct Element **head) {
    struct Element *current = *head;
    struct Element *next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }

    *head = NULL;
}
