#include <iostream>

std::string DNAtoRNA(std::string dna){
    int dna_size = dna.length();
    char *rna = new char[dna_size];


    for (int i = 0; i < dna_size; ++i) {
        std::cout<< dna[i];
        if (dna[i] == 'T')
            rna[i] = 'U';
        else
            rna[i] = dna[i];
    }
    return rna;
}
