#include "List.h"
#include "string.h"


NODE* initList(const DATA* data){
    NODE* head = (NODE*)malloc(sizeof(NODE));
    head->data=data;
    head->next = NULL;
    return head;
}

NODE* createNode(const DATA* data){
    NODE* tmp = (NODE*) malloc(sizeof(NODE));
    tmp->data=data;
    tmp->next = NULL;
    return tmp;
}

void addTail(NODE* const head, const DATA* data){
    NODE* next = head;
    while(next->next != NULL){
        printf("%d", next);
        next = next->next;
    }
    next->next=createNode(data);
}

void addHead(NODE** head, const DATA* data){
    NODE* tmp = (*head);
    (*head) = createNode(data);
    (*head)->next=tmp;
}

void addSorted(NODE** head, const DATA* data){
    NODE* next = (*head)->next;
    NODE* prev = (*head)->next;
    while(next != NULL && next->data->num < data->num){
        prev = next;
        next = next->next;
    }

    if(next == (*head) && next == prev){
        addHead(head, data);
    }

    else{
        NODE* tmp = createNode(data);
        prev->next = tmp;
        tmp->next = next;
    }
}

NODE* getByString(const NODE* const head, char* str){
    NODE* next = head;
    while(next != NULL){
        if(strcmp(next->data->text, str)){
            return next;
        }
        next = next->next;
    }
    return NULL;
}
NODE* getByNum(const NODE* const head, int num){
    NODE* next = head;
    while(next != NULL){
        if(num == next->data->num){
            return next;
        }
        next = next->next;
    }
    return NULL;
}

void removeByNum(NODE** head, int num){
    if((*head)->data->num == num){
        NODE* tmp = *head;
        *head = tmp->next;
        tmp->next = NULL;
        free(tmp->data);
        free(tmp);
        return;
    }

    NODE* next = (*head)->next;
    NODE* prev = *head;

    if(next == NULL){
        if(prev->data->num == num){
            free((*head)->data);
            free(*head);
            *head = NULL;
        }
        return;
    }

    while(next != NULL)
    {
        if(num == next->data->num){
            prev->next = next->next;
            next->next = NULL;
            free(next->data);
            free(next);
            return;
        }
    }
}

DATA* createData(const char* text, int num) {
    DATA* newData = (DATA*) malloc(sizeof(DATA));

    newData->text = malloc(strlen(text) + 1);
    if (newData->text == NULL) {
        exit(1);
    }
    strcpy(newData->text, text);

    newData->num = num;

    return newData;
}


void print(const NODE* const head){
    NODE* next = head;
    while(next != NULL){
        printf("%s %d\n", next->data->text, next->data->num);
        next = next->next;
    }
}