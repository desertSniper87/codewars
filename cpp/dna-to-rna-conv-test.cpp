#include <igloo/igloo_alt.h>
#include "dna-to-rna-conv.cpp"

Describe(DNA_to_RNA)
{
    It(Sample_Test)
    {
        Assert::That(DNAtoRNA("GCAT"), Equals("GCAU"));
    }

};
