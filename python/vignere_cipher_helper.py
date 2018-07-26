#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author            : desertsniper87 <torshobuet@gmail.com>
# Date              : 16.07.2018
# Last Modified Date: 16.07.2018
class VigenereCipher:
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        result = ''
        for idx, i in enumerate(text):
            if i in self.alphabet:
                # print((i), (self.alphabet[idx]), (self.key[idx%len(self.alphabet)]))
                # key += self.key[idx%len(self.alphabet)]
                result += self.alphabet[
                                        (
                                         self.alphabet.index(i)+
                                         self.alphabet.index(
                                                             self.key[idx%len(self.key)]
                                                            )
                                        ) %len(self.alphabet)
                                       ]
            else:
                result += i
        return result



        
    
    def decode(self, text):
        result = ''
        for idx, i in enumerate(text):
            if i in self.alphabet:
                result += self.alphabet[
                                        (
                                         self.alphabet.index(i)-
                                         self.alphabet.index(
                                                             self.key[idx%len(self.key)]
                                                            )
                                        )%len(self.alphabet)
                                       ]
            else:
                result += i
        return result

