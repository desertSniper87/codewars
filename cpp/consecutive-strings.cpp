#include <iostream>

#include <string>
#include <vector>

class LongestConsec {
public:
    static std::string longestConsec(std::vector<std::string> &strarr, int k);
    static bool compareLen(const std::string& a, const std::string& b) {
        return (a.size() > b.size());
    }
};

std::string LongestConsec::longestConsec(std::vector<std::string> &strarr, int k) {
/*    for (const auto &item : strarr) {
        std::cout<< item.length()<< std::endl;
    }*/
    std::vector<std::string> &array = strarr;
    std::vector<std::string> concat_string_container;
    std::string cat_string;
    for (int i = 0; i < array.size()-1; ++i) {
//        std::cout<< array[i]<< ' '<< array[i].length()<< ' '<< array[i+1]<< array[i+1].length()<< std::endl;
        cat_string = array[i] + array[i + 1];
        concat_string_container.push_back(cat_string);
    }

//    std::cout<< k;
    std::sort(concat_string_container.begin(), concat_string_container.end(), compareLen);

    for (const auto &item : concat_string_container) {
        std::cout<< item<< std::endl;
    }

    return concat_string_container.front();;
}


