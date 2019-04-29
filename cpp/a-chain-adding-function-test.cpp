#include <igloo/igloo_alt.h>
using namespace igloo;

#include "a-chain-adding-function.cpp"

#include <iostream>

Describe(test_add)
{
    It(should_pass_some_example_tests)
    {
        std::cout << "add(1) == 1\n";
        Assert::That(add(1), Equals(1));
        std::cout << "add(1)(2) == 3\n";
        Assert::That(add(1)(2), Equals(3));
        std::cout << "add(1)(2)(3) == 6\n";
        Assert::That(add(1)(2)(3), Equals(6));
    }
};


int main(int argc, const char *argv[]) {
    return TestRunner::RunAllTests(argc, const_cast<char **>(argv));
}
