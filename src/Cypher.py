import pandas as pd

class Cypher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def __str__(self):
        return self.alphabet

    # ===== Setters =====
    def setKey(self, key):
        self.key = key

    def setAlphabet(self, abc):
        self.alphabet = abc

    # ===== Getters =====
    def getKey(self):
        return self.key

    def getAlphabet(self):
        return self.alphabet

    # ===== Methods =====
    def encode(self, str):
        result = ""
        fullKey = self.stretchKey(str)

        for character_i in range(0, len(str)):
            if (self.alphabet.find(str[character_i]) != -1):
                result += self.shiftChar(str[character_i], fullKey[character_i])
            else:
                result += str[character_i]
        return result

    def decode(self, str):
        result = ""
        fullKey = self.stretchKey(str)

        for character_i in range(0, len(str)):
            if (self.alphabet.find(str[character_i]) != -1):
                result += self.deshiftChar(str[character_i], fullKey[character_i])
            else:
                result += str[character_i]
        return result

    def stretchKey(self, str):
        result = ""

        while (len(result) <= len(str)):
            result += self.key

        return result[0:len(str)]

    def shiftChar(self, char, shiftChar):
        shift = self.alphabet.find(shiftChar)
        shiftedValue = self.alphabet.find(char) + shift

        if (shiftedValue >= len(self.alphabet)):
            shiftedValue -= len(self.alphabet)

        return self.alphabet[shiftedValue]

    def deshiftChar(self, char, shiftChar):
        shift = self.alphabet.find(shiftChar)
        shiftedValue = self.alphabet.find(char) - shift

        if (shiftedValue < 0):
            shiftedValue += len(self.alphabet)

        return self.alphabet[shiftedValue]

def test():
    df = pd.read_csv('~/.c/cyphers.csv')

    print(df)

    test_cypher = Cypher("iamthedanger", "6aA7!bB8@cC9#dD$eE%fF^gG&hH*iI(jJ)kK-lL=mM_nN+oO,pP.qQ'rR;sS:tT/uU0vV1wW2xX3yY4zZ5")

if __name__ == "__main__":
    test()