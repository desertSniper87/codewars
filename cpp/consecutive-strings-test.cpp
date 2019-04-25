#include <igloo/igloo_alt.h>
using namespace igloo;

#include "consecutive-strings.cpp"

#include <string>
#include <vector>

void testequal(std::string ans, std::string sol) {
    Assert::That(ans, Equals(sol));
}

void dotest(std::vector<std::string> arr, int k, std::string expected) {
    testequal(LongestConsec::longestConsec(arr, k), expected);
}

Describe(longestConsec_Tests) {
    It(Fixed__Tests)
    {
        std::vector<std::string> arr = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
        dotest(arr, 2, "abigailtheta");
        arr = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
        dotest(arr, 1, "oocccffuucccjjjkkkjyyyeehh");
    }
};


int main(int argc, const char *argv[]) {
    return TestRunner::RunAllTests(argc, const_cast<char **>(argv));
}
