#include <igloo/igloo_alt.h>
using namespace igloo;

#include "dna-to-rna-conv.cpp"

Describe(DNA_to_RNA)
{
    It(Sample_Test)
    {
        Assert::That(DNAtoRNA("GCAT"), Equals("GCAU"));
    }

};

int main(int argc, const char *argv[])
{
    return TestRunner::RunAllTests(argc, const_cast<char **>(argv));
}
