#include <stdio.h>

// "Preloaded Code" (do NOT modify!)
typedef struct node {
  int data;
  struct node *next;
} Node;

// Main Solution
char *stringify(Node *list) {
  // TODO: Return a string representation of the linked list provided
  char* ch = NULL;
  int i = 0;
  while(list->next != NULL) {
      ch[i++] = list->data;
      list = list->next;
  }
  ch[++i] = '\0';
  return ch;
}

