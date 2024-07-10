#include "stdlib.h"
#include "stdio.h"

#define SIZEOFTEXT 50

typedef struct node{
    char text[SIZEOFTEXT];
    int number;
    struct NODE* next;
}NODE;

NODE* createNode(char text[SIZEOFTEXT],int number);
void addEnd(NODE** list,char text[SIZEOFTEXT],int number);
void addHead(NODE** list,char text[SIZEOFTEXT],int number);
void addAfter(NODE* lsit,char text[SIZEOFTEXT],int number,int prevInt);
NODE* findNode(NODE* list,int number);
int deleteNode(NODE** list,int number);
void printList(NODE* list);

NODE* createNode(char text[SIZEOFTEXT],int number){
    NODE* new=(NODE*)malloc(sizeof(NODE));
    strncpy(new->text,text,50);
    new->number=number;
    new->next=NULL;
    return new;
}

void addEnd(NODE **list,char text[SIZEOFTEXT],int number){

    NODE* new=createNode(text,number);
    
    NODE* tmp=*list;
    if(*list==NULL){
        *list=new;
        return;
    }
    while(tmp->next!=NULL){
        tmp=tmp->next;
    }
    tmp->next=new;
}

void addBegin(NODE** list,char text[SIZEOFTEXT],int number){
    NODE* head=createNode(text,number);
    head->next=*list;
    (*list)=head;
}

void addAfter(NODE* list,char text[SIZEOFTEXT],int number,int prevInt){
    NODE* new=createNode(text,number);
    NODE* tmp=list;
    while(tmp->number!=prevInt){
        tmp=tmp->next;
        if(tmp->next==NULL)
            break;
    }
    if(tmp->next!=NULL){
        new->next=tmp->next;
        tmp->next=new;
    }else{
        tmp->next=new;
    }

}

NODE* findNode(NODE* list,int number){
    NODE* tmp=list;
    NODE* result=NULL;
    while(tmp->number!=number){
        tmp=tmp->next;
        if(tmp->next==NULL)
            break;
    }
    if(tmp->next==NULL && tmp->number!=number){
        return result;
    }
    result=tmp;
    return result;
}

int deleteNode(NODE** list,int number){
    NODE* tmp=*list;
    NODE* prev=NULL;
    if(tmp!=NULL && tmp->number==number){
        *list=tmp->next;
        free(tmp);
        return 1;
    }
    while(tmp->number!=number){
        prev=tmp;
        tmp=tmp->next;
        if(tmp->next=NULL)
            break;
    }
    if(tmp==NULL){
        return 0;
    }
    prev->next=tmp->next;
    free(tmp);

}

void printList(NODE* list){
    while(list!=NULL){
        printf("%d-%s\n",list->number,list->text);
        list=list->next;
    }
}



int main(){

    NODE* list=NULL;
   addBegin(&list,"first",1);
    
    addEnd(&list,"last",5);
    addAfter(list,"after",3,1);
    
    printList(list);
    NODE* find=findNode(list,3);
    if(find!=NULL){
        printf("Node exists in list, %d,%s\n",find->number,find->text);
    }else{
        printf("Node does not exists in list\n");
    }
    int deleted=deleteNode(&list,1);
    if(deleted!=0){
        printf("Node deleted successful\n");
    }else{
        printf("Node can not been deleted\n");
    }
    printList(list);

}
