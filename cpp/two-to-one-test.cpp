#include <igloo/igloo_alt.h>
using namespace igloo;

#include "two-to-one.cpp"

#include <string>

void testequal(std::string ans, std::string sol) {
    Assert::That(ans, Equals(sol));
}
void dotest(std::string a1, std::string a2, std::string expected)
{
    testequal(TwoToOne::longest(a1, a2), expected);
}

Describe(longest_Tests)
{
    It(Fixed__Tests)
    {
        dotest("aretheyhere", "yestheyarehere", "aehrsty");
        dotest("loopingisfunbutdangerous", "lessdangerousthancoding", "abcdefghilnoprstu");
    }
};

int main(int argc, const char *argv[])
{
    return TestRunner::RunAllTests(argc, const_cast<char **>(argv));
}

