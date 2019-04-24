import unittest


from most_frequent_word import *


class WordTest(unittest.TestCase):
    def test_func(self):
        # self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        # self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])
        self.assertEqual(top_3_words("  , e   .. "), ["e"])
        self.assertEqual(top_3_words("  ...  "), [])
        self.assertEqual(top_3_words("  '  "), [])
        self.assertEqual(top_3_words("  '''  "), [])
        self.assertEqual(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
        self.assertEqual(top_3_words("oxmqU_ ;.Mbyu-;zLNnSP_sfJ-! :oxmqU,,UXPtMy.,.,!UXPtMy:!-_oxmqU:OLleCVMxsh_:_,:DlsDQlzDu! Mbyu_!IGUbrcG-?_?!sfJ-?zLNnSP: IGUbrcG:_?zLNnSP?DlsDQlzDu/iWLCk,;Mbyu_.__,UXPtMy :?.;jlZRZgOW'!/zLNnSP?UXPtMy,! OLleCVMxsh_,!,?Mbyu :_ -sfJ-/-, zLNnSP,-/,/rsTGcxbCe?!/.-rsTGcxbCe.oxmqU._;:DlsDQlzDu;;;-UXPtMy/!zLNnSP!?!!zLNnSP_-.,!IGUbrcG!?:?/IGUbrcG/sfJ-!rNup-;:.:OLleCVMxsh._/!,UXPtMy/,,UXPtMy,-?iWLCk;,;-,DlsDQlzDu:_-/,jlZRZgOW',.;??UXPtMy,,.!:DlsDQlzDu ..//jlZRZgOW';_?. UXPtMy..-iWLCk.zLNnSP,!;zLNnSP__UXPtMy.!oxmqU-,sfJ!:-/UXPtMy,.?/_OLleCVMxsh:;.rsTGcxbCe,?__OLleCVMxsh/_;;Mbyu ,jlZRZgOW'.._,!jlZRZgOW'-,sfJ?jlZRZgOW':OLleCVMxsh:DlsDQlzDu/ sfJ-rsTGcxbCe:!:jlZRZgOW'/- -;jlZRZgOW'._sfJ//-oxmqU;:-?/rsTGcxbCe?; _ oxmqU -;UXPtMy:?DlsDQlzDu.zLNnSP,:-/!jlZRZgOW',-_: zLNnSP_ _/DlsDQlzDu-?rsTGcxbCe:?-_rsTGcxbCe_..?-UXPtMy,_;.sfJ?!:/UXPtMy! //rsTGcxbCe;.?-rsTGcxbCe;;  sfJ!zLNnSP_QViKU : ;rsTGcxbCe/;-;;sfJ;:iWLCk;!-.sfJ__,._IGUbrcG: --?iWLCk-:IGUbrcG-UXPtMy_;-!jlZRZgOW'.?,;iWLCk:UXPtMy: , DlsDQlzDu!;OLleCVMxsh,;:/Mbyu,/:_UXPtMy/?; DlsDQlzDu:;oxmqU!Mbyu?zLNnSP,!rsTGcxbCe?_DlsDQlzDu;:.jlZRZgOW';_!zLNnSP  /Mbyu,;;!sfJ/_/QViKU./.,rsTGcxbCe -jlZRZgOW',zLNnSP-UXPtMy/DlsDQlzDu?-?..Mbyu:-.UXPtMy_!-:zLNnSP,iWLCk!DlsDQlzDu!-:-zLNnSP :.!iWLCk;zLNnSP_jlZRZgOW'; -,?oxmqU-;-:rsTGcxbCe_jlZRZgOW'-:_UXPtMy-UXPtMy?zLNnSP, ._-DlsDQlzDu,/.;,IGUbrcG;:.zLNnSP-,rsTGcxbCe:::!UXPtMy ;:?rsTGcxbCe-.oxmqU- jlZRZgOW', :;QViKU Mbyu:;//OLleCVMxsh_UXPtMy_-rsTGcxbCe_-.zLNnSP:oxmqU ?_?Mbyu,/!oxmqU .-:zLNnSP/-;oxmqU-/_;;IGUbrcG jlZRZgOW'./,-DlsDQlzDu,.//_sfJ. ,oxmqU-!_Mbyu-_:;IGUbrcG,:-;OLleCVMxsh-__/ rsTGcxbCe.._:jlZRZgOW'..! UXPtMy.-;oxmqU-?!rsTGcxbCe.?oxmqU !?/ rsTGcxbCe?//UXPtMy,zLNnSP;!rsTGcxbCe,!-,-Mbyu?,:iWLCk.-;_sfJ;?!.,rsTGcxbCe-?- !iWLCk?iWLCk-zLNnSP DlsDQlzDu;/,/rNup./;jlZRZgOW':?zLNnSP/;__-Mbyu..;.,zLNnSP-/;; Mbyu!oxmqU; :-:DlsDQlzDu.rsTGcxbCe::,OLleCVMxsh:?IGUbrcG;__jlZRZgOW':-;;/sfJ _!-_IGUbrcG,,.:/zLNnSP/DlsDQlzDu__/;oxmqU?IGUbrcG,_!, QViKU!rsTGcxbCe, _sfJ.?-!UXPtMy,;-iWLCk:/:IGUbrcG!jlZRZgOW'_jlZRZgOW' !Mbyu;  ?UXPtMy,?/;:rsTGcxbCe?: zLNnSP/zLNnSP._:;!oxmqU/ __:jlZRZgOW'-_?"), ['zlnnsp', 'uxptmy', 'rstgcxbce'])

        self.assertEqual(top_3_words("SvQDwZJoX?SvQDwZJoX.-:?;snBfRl?snBfRl snBfRl _! SvQDwZJoX;//:/SvQDwZJoX_/-,-SvQDwZJoX/SvQDwZJoX,;/-_snBfRl_snBfRl./.!yVX:!_;snBfRl;_;;/snBfRl;snBfRl!,:--yVX.?,,_SvQDwZJoX!?-:/snBfRl SvQDwZJoX?_.yVX-,yVX:SvQDwZJoX  _snBfRl:yVX.-?-.SvQDwZJoX snBfRl??yVX?yVX-snBfRl,yVX.-,/ yVX-_snBfRl.?SvQDwZJoX!__,:yVX/. yVX.;?;yVX-::snBfRl:/!/yVX!yVX _;!SvQDwZJoX;;.?SvQDwZJoX.snBfRl?SvQDwZJoX!;,.snBfRl--yVX-: SvQDwZJoX -!-SvQDwZJoX,,/:/yVX,,SvQDwZJoX-._-yVX,: :SvQDwZJoX?;?;SvQDwZJoX_ snBfRl,!yVX.-??-"), ['svqdwzjox', 'yvx', 'snbfrl'])

        self.assertEqual(top_3_words("SKUlg.,!/SKUlg?SKUlg ,,:;GS''CfWH-_?SKUlg./::!SKUlg;!SKUlg;;GS''CfWH_ _.!SKUlg-/ .SKUlg_?:.GS''CfWH!_;GS''CfWH:!/GS''CfWH:_"), ['skulg', "gs''cfwh"])
def main():
        unittest.main()

if __name__ == "__main__":
    main()

