#include <stdio.h>
#include "LinkedList.h"

/*TEST APP*/
int main()
{
    NODE* head = NULL;

    addFront(&head, 1193, "Anja");
    addFront(&head, 1173, "Dejana");
    addRear(&head, 1179, "Ana");

    printf("Initial list:\n");
    printList(head);
    printf("\n");

    int_least32_t id_to_delete = 1173;
    char name_to_delete[max_num] = "Dejana";
    int_least32_t delete_result = deleteByIdAndName(&head, id_to_delete, name_to_delete);

    if (delete_result == 0) {
        printf("Deleted node with ID %d and name %s.\n\n", id_to_delete, name_to_delete);
    } else {
        printf("Failed to delete node with ID %d and name %s.\n\n", id_to_delete, name_to_delete);
    }

    printf("Updated list:\n");
    printList(head);
	free(head);
    return 0;
}
