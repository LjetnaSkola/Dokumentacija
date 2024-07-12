struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

/*  insert a new node at the beginning of a linked list */
int insert_at_beggining(struct Node** head, int data);

/*  insert a new node at the end of a linked list */
int insert_at_end(struct Node** head, int data);

/*  insert a new node after specified node of a linked list */
int insert_after(struct Node** head, int after, int data);

/*  insert a new node before specified node of a linked list */
int insert_before(struct Node** head, int before, int data);

/* Function to create a new node */
struct Node* createNode(int data);

/* delete a node at the beginning of a linked list  */
int delete_from_beggining(struct Node** head);

/* delete a node at the end of a linked list  */
int delete_from_end(struct Node** head);

/* delete a specific node of a linked list  */
int delete_data(struct Node** head, int data);

/* finding the specified node of a linked list */
struct Node* find(struct Node** head, int data);
