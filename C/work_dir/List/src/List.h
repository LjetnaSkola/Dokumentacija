#include "stdio.h"
#include "stdlib.h"

struct dat;
struct node;



typedef struct dat{
    char* text;
    int num;
}DATA;

typedef struct node{
    DATA* data;
    struct NODE* next;
}NODE;


NODE* initList(const DATA* data);

DATA* createData(const char* text, int num);
NODE* createNode(const DATA* data);

void addTail(NODE* const head, const DATA* data);
void addHead(NODE** head, const DATA* data);
void addSorted(NODE** head, const DATA* data);

NODE* getByString(const NODE* const head, char* str);
NODE* getByNum(const NODE* const head, int num);
void removeByNum(NODE** head, int num);

void print(const NODE* const head);