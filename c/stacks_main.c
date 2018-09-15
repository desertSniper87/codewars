#include "stacks.c"
#include <stdio.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdlib.h>

void stack_push(Stack *stack, int data);
int stack_pop(Stack *stack);
int stack_peek(const Stack *stack);
bool stack_is_empty(const Stack *stack);

Stack *new_stack() {
  Stack *stack = malloc(sizeof(Stack));
  stack->root = NULL;
  return stack;
}

void delete_stack(Stack *stack) {
  Node *nd = stack->root;
  while (nd) {
    Node *tmp = nd->next;
    free(nd);
    nd = tmp;
  }
  free(stack);
}

int main() {
    Stack *stack = new_stack();
    stack_push(stack, 1);

    return 0;

}
