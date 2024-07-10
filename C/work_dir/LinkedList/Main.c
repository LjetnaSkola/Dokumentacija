#include "stdio.h"
#include "LinkedList.h"

int main()
{
    NODE *head = 0;
    for(int i = 0; i <= 5; i++)
    {
        add(&head, i);
    }
    print(head);
    if(delete1(&head, 3))
        printf("Cvor sa vrijednoscu 3 je obrisan.");
    else
        printf("Cvor sa vrijednoscu 3 nije obrisan.");
}