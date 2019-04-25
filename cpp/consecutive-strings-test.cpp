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
        std::vector<std::string> arr;

        arr = {"zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail"};
        dotest(arr, 2, "abigailtheta");

        arr = {"ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh"};
        dotest(arr, 1, "oocccffuucccjjjkkkjyyyeehh");

        arr = {};
        dotest(arr, 1, "");

        arr = {"itvayloxrp", "wkppqsztdkmvcuwvereiupccauycnjutlv", "vweqilsfytihvrzlaodfixoyxvyuyvgpck" };
        dotest(arr, 2, "wkppqsztdkmvcuwvereiupccauycnjutlvvweqilsfytihvrzlaodfixoyxvyuyvgpck");

        arr = {"it", "wkppv", "ixoyx", "3452", "zzzzzzzzzzzz"};
        dotest(arr, 15, "");

//        arr = {"NJIgbfGjI", "DihcFaEXc", "rqDfQjHflKMpBvWsuLAeXUNl",
//               "pAsYNRfWzpOkPPzGcZccc", "sYwtcVwm", "DlXYJaFpzuPCKD",
//               "dEqCCaJiIEtGkBQUjjchcPVu", "hwUvaKMbVMBCHEO", "PVZjWNWlxLdtV",
//               "zFwnejrnjpxvsraxFoVnra", "nESoOKfPzyvfuodZPZ", "IABmeezq",
//               "UeUjwQerhxPTc", "NrczdyVtYbEFgKNsRtlcVYPdl",
//               "WxQOjSzIlBAXFCSeHwlH", "YYjdgT", "veaasDKMYVKClywcmTlCY",
//               "iYYWdowCUHfkexitR", "xZoDpcwJLgb", "egKXwHH",
//               "CeMcRvbsjPBPHMkUPsJ", "pUQnDTpqGAYfhaMbNE", "nxcntCcmgUmwULr",
//               "KOUKiHsBuLSRDg", "tquNfHnPPMbUT", "LGAuuCyOu", "mlDAImCvfRbR",
//               "cMFbpWCCmQDgNPl", "LOxVeqTZZKjysXhalWmyE", "kDljX",
//               "OGCWmgbfCjPqkNtou", "LsHqntlMcLddaOJ",
//               "mFmmkXWnIiSGjQHmQdQZmva", "pehZeQqGKc", "deJDq", "eCtnWcvsH",
//               "YTYBeqZcxcUDmZuxKzW", "qbqvfKPDDNBxkJYpYWbYlkeDK",
//               "NNnKcJwXCaWwiSaBg", "QXYxfMQJEMkLWleznpioNwaI"};
//        dotest(arr, 6, "zFwnejrnjpxvsraxFoVnranESoOKfPzyvfuodZPZIABmeezqUeUjwQerhxPTcNrczdyVtYbEFgKNsRtlcVYPdlWxQOjSzIlBAXFCSeHwlH");

        arr = {"zJHRMo", "YZVFKMLsTspcFoBYyCKDf", "BvMMsewgWtAOoE",
            "MexOYiTUqdTvKoGuDlZamkiA", "EyALdiAfdvdNYceTwvKwn",
            "wmtTiyIWwlnhJfvoh", "mobVtCoMRxVgjZLHxctaE", "swwbmNOzyqjeE",
            "qMaUuD", "WEXfZG", "bLBKqOWlqeNykeXDFWDlkcWR",
            "aaaxQmXgPLtaFVAwrpgzt", "mxjuUZPqUUIdqnJyznEEl", "WExTKDrp",
            "AXYBjjgmxi", "fJaYay", "XdBsTJ", "XXdpgozG", "VAiaOyFURDABp",
            "JyKQLc", "MqLXTJBXQsetjlogiLh", "fHczQo", "lzacAiB", "llrTXtPt",
            "bkwvIMYiEzUY", "FDfcjMqE"};
        dotest(arr, 1, "MexOYiTUqdTvKoGuDlZamkiA");

        arr = {"uNATikZuSBNSxaHLubuOg", "jOuWzzvYeRKNrrPiRrLfB",
            "kNbQFwgWpGtXzyWpPeGoVqxj", "dhKRSSobVLeFOMTk",
            "ctgMvOLZFXWlvyrbAuIB", "SBnenPDsCr", "WhUwPhLoPVhONZgxQLfjgGUm",
            "RVzwZLBNhYluuGvPOewTN", "XkTxgOXcktNKNKvPKb", "rxdXLFteTytVKRC",
            "bFUWxeJpyWsMc", "libFErIfOBYROR", "ydwjZfCZUKxjBXJU",
            "iCmUBqMkORQg", "jWLzbHmMSyTGxHGH", "xLnHkVPDZHAocvnW",
            "pXeCuzMSUzhevLucgmFBEoG", "LWjuuALQriknIN",
            "GQsBQqCBMLJPDVgshoWzXBtkt", "vjYFoPDzleQfwW",
            "XiDhALCXveyrOLIetwEmHIDG", "baBscpjsqacjDUtMgyLRzTFMc", "JRziP",
            "keQgGgOnILaQkrcgvVXN", "jGWDtjyXFbqgXLeLNvzlo", "PVoBUKBmtWBXApD",
            "tWArSntoYylDSFsSpgKxMvRa", "hcGsra", "nKavRNXgDCWpzJqUsR",
            "EGLpIpOnJ", "ntQTiGrkicHvNJEoiferJoprn"};

        dotest(arr, 1, "GQsBQqCBMLJPDVgshoWzXBtkt");
    }
};


int main(int argc, const char *argv[]) {
    return TestRunner::RunAllTests(argc, const_cast<char **>(argv));
}
