#include "stdio.h"
#include "stdlib.h"

typedef struct Data{
    int m_num;
    char* m_string;
}Data;

typedef struct Node{
    Data m_data;
    struct Node* m_next;
}Node;

void addNode(Node* node, Node** head){
    if(*head == NULL){
        *head = malloc(sizeof(Node*));
        *head = node;
    }
    else{
        Node *last = *head;
        while(last->m_next){
            last = last->m_next;
        }
        last->m_next = node;
    }
}

void printList(Node* head){
    printf("================\n");
    while(head != NULL){
        printf("%d (%s)\n", head->m_data.m_num, head->m_data.m_string);
        head = head->m_next;
    }
    printf("================\n");
}

void removeNode(Node** head, int index){
    Node* iterator = (*head);
    while(iterator != NULL){
        Node* del = (iterator)->m_next;
        if((iterator)->m_data.m_num == index){
                (iterator)->m_data = del->m_data;
                (iterator)->m_next = del->m_next;
                del = NULL;
                free(del);

            return;
            
        }

        iterator = (iterator)->m_next;
    }
}

Node* searcheNode(Node* head, int index){
    while(head != NULL){
        if((head)->m_data.m_num == index){
            return head;
        }

        head = (head)->m_next;
    }
}
