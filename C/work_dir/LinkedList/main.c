#include "stdio.h"
#include "LinkedList.h"
#include "stdlib.h"

int main(){
    Node *head = NULL;
    Node *first = malloc(sizeof(Node));
    first->m_data.m_num = 1;
    first->m_data.m_string = "Jedan";
    first->m_next = NULL;

    Node *second = malloc(sizeof(Node));
    second->m_data.m_num = 2;
    second->m_data.m_string = "Dva";
    second->m_next = NULL;

    Node *third = malloc(sizeof(Node));
    third->m_data.m_num = 3;
    third->m_data.m_string = "Tri";
    third->m_next = NULL;

    addNode(first, &head);
    addNode(second, &head);
    addNode(third, &head);

    printList(head);

    removeNode(&head, 2);
    printList(head);

    Node* search = searcheNode(head, 3);
    printf("%d (%s)\n", search->m_data.m_num, search->m_data.m_string);
    printf("================\n");
}
