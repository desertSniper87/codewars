#include <stdbool.h>
#include <stdlib.h>

// Key definitions
// Please do not modify them - attempts to do so
// may lead to unexpected behavior

// A node in our linked list
typedef struct node {
    int data;
    struct node *next;
} Node;

// Our stack, implemented as a wrapper around our linked list
typedef struct {
    Node *root;
} Stack;

// Modify the code below to implement the key operations for our stack
void stack_push(Stack *stack, int data) {
    Node* old_root = stack->root;

    Node* new_node = (Node*) malloc (sizeof(Node));
    new_node->data = data;
    new_node->next = old_root;
    stack->root = new_node;
}
int stack_pop(Stack *stack) {
    int ret = stack->root->data;
    stack->root = stack->root->next;

    return ret; 
}
int stack_peek(const Stack *stack) {
    return stack->root->data;
}
bool stack_is_empty(const Stack *stack) {
    if (stack->root==NULL) {
        return true;
    }
    return false; 
}
