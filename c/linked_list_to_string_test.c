#include <criterion/criterion.h>
#include <stddef.h>
#include "linked_list_to_string.c"

/*typedef struct node {*/
  /*int data;*/
  /*struct node *next;*/
/*} Node;*/

char *stringify(Node *);

Test(stringify, should_work_for_code_examples_provided_in_the_description) {
  cr_assert_str_eq("1 -> 2 -> 3 -> NULL", stringify(&((Node){
    .data = 1,
    .next = &((Node){
      .data = 2,
      .next = &((Node){
        .data = 3,
        .next = NULL
      })
    })
  })));
  cr_assert_str_eq("0 -> 1 -> 4 -> 9 -> 16 -> NULL", stringify(&((Node){
    .data = 0,
    .next = &((Node){
      .data = 1,
      .next = &((Node){
        .data = 4,
        .next = &((Node){
          .data = 9,
          .next = &((Node){
            .data = 16,
            .next = NULL
          })
        })
      })
    })
  })));
  cr_assert_str_eq("NULL", stringify(NULL));
}
