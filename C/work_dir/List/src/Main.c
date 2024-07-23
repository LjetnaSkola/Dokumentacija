#include "List.h"

int main(){
    DATA* d = createData("d1", 1);
    NODE* head = (NODE*) malloc(sizeof(NODE));
    head->data = d;
    head->next = NULL;
    addTail(head, createData("d2", 2));
    addHead(&head, createData("d3", 3));
    print(head);
    removeByNum(&head, 3);
    print(head);

    return 0;
}