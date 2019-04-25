#include <iostream>

#include <string>
#include <vector>

class LongestConsec {
public:
    static std::string longestConsec(std::vector<std::string> &strarr, int k);
    static bool compareLenReverse(const std::string &a, const std::string &b) {
        return (a.size() > b.size());
    }
//    static bool compareAlpha(const std::string& a, const std::string& b) {
//        return (a < b);
//    }
    static bool compareLen(const std::string &a, const std::string &b) {
        return (a.size() < b.size());
    }
};

std::string LongestConsec::longestConsec(std::vector<std::string> &strarr, int k) {
    std::vector<std::string> &string_container = strarr;
    std::vector<std::string> concat_string_container;
    std::string cat_string;

    int size_of_vector = string_container.size();

    if (k>size_of_vector){
        return "";
    }

    std::cout<< std::endl<< "************  "<< k<< "  **************"<< std::endl;

    for (const auto &item : string_container) {
        std::cout<< item<< ' ';
    }

    std::cout<< std::endl;

    if (string_container.empty() == 1){
        return "";
    }

    if (k == 1){
        std::string max_elem = *std::max_element(string_container.begin(), string_container.end(), compareLen);
        std::cout<< max_elem<< ' '<< max_elem.length();

        for (const auto &item : string_container) {
            if (item.length() == max_elem.length())
                return item;
        }
    } else {
        for (int i = 0; i < size_of_vector-k+1; ++i) {
            cat_string = "";
            for (int j = i; j<k+i; ++j) {
                cat_string += string_container[j];
            }
            concat_string_container.push_back(cat_string);
        }

        std::string max_elem = *std::max_element(concat_string_container.begin(), concat_string_container.end(),
                                                 compareLen);

        std::cout<< max_elem<< ' '<< max_elem.length();

        for (const auto &item : concat_string_container) {
            if (item.length() == max_elem.length())
                return item;
        }
    }
}


