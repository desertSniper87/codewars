class CaesarCipher:
    alphaSet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    def __init__(self, shift):
        self.shift = shift

    def encode(self, str):
        result = ''
        for i in str.upper():
            if i in self.alphaSet:
                result += self.alphaSet[
                        (self.alphaSet.index(i) + self.shift) 
                                        % len(self.alphaSet)
                                       ]
            else:
                result += i
        return result
        
    def decode(self, str):
        result = ''
        for i in str:
            if i in self.alphaSet:
                result += self.alphaSet[
                        (self.alphaSet.index(i) - self.shift) 
                                        % len(self.alphaSet)
                                       ]
            else:
                result += i
        return result
