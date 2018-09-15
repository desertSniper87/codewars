#include <criterion/criterion.h>

int find_smallest_int(int *array, int size);

static void test_one(int *array, int size) {
  int min = array[0];
  for (int i = 1; i < size; ++i) if (array[i] < min) min = array[i];
  int actual = find_smallest_int(array, size);
  cr_assert_eq(actual, min, "Expected: %d Actual: %d", min, actual);
}

Test(smallest_test, fixed_test) {
  test_one((int[]){34, 15, 88, 2}, 4);
  test_one((int[]){34, -345, -1, 100}, 4);
  test_one((int[]){78, 56, 232, 12, 11, 43}, 6);
}
