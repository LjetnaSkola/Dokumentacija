#include "linked-list.h"

int main()
{
    LINKED_LIST list = {NULL, NULL};
    LINKED_LIST_NODE monday = {1, "lecture git", NULL};
    LINKED_LIST_NODE tuesday = {2, "lecture c types", NULL};
    LINKED_LIST_NODE wednesday = {3, "lecture c data structures", NULL};
    LINKED_LIST_NODE pointers = {4, "lecture c pointers", NULL};

    addHead(&list, &monday);
    addTail(&list, &tuesday);
    addNext(&list, &tuesday, &wednesday);
    addNext(&list, &monday, &pointers);

    printList(&list);

    if (findById(&list, tuesday.id) == &tuesday)
    {
        printf("Success find by id\n");
    };
    if (findByName(&list, pointers.name) == &pointers)
    {
        printf("Success find by name\n");
    };

    removeNode(&list, pointers.id);
    printList(&list);

    return EXIT_SUCCESS;
}
