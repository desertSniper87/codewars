#include <iostream>
#include <vector>

class TwoToOne {
public:
    static std::string longest(const std::string &s1, const std::string &s2);
};

std::string TwoToOne::longest(const std::string &s1, const std::string &s2) {
    std::vector<char> v;

    for (int i = 0; i < s1.length(); ++i) {
        v.push_back(s1[i]);
    }

    for (int i = 0; i < s2.length(); ++i) {
        v.push_back(s2[i]);
    }


    sort(v.begin(), v.end());

    std::vector<char>::iterator it;
    it = std::unique(v.begin(), v.end());

    v.erase(it, v.end());

    std::string str(v.begin(), v.end());

    return str;
}
