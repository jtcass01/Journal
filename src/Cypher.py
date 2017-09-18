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

    def encode_file(self, file_location, file_destination = None):

        if file_destination == None:
            with open(file_location, 'r') as read_file:
                data = read_file.readlines()
            for line in data:
                print(self.encode(line[:-1]), 'encoded')
                print(self.decode(self.encode(line[:-1])), 're-decoded')
        else:
            with open(file_location, 'r') as read_file:
                data = read_file.readlines()

            with open(file_destination, 'w') as write_file:
                for line in data:
                    print("writing...", self.encode(line[:-1]))
                    write_file.write(self.encode(line))
                    write_file.flush()

    def decode_file(self, file_location, file_destination = None):
        data = None

        if file_destination == None:
            with open(file_location, 'r') as read_file:
                data = read_file.readlines()
            for line in data:
                print(self.decode(line[:-1]))
        else:
            with open(file_location, 'r') as read_file:
                data = read_file.readlines()
            with open(file_destination, 'w') as write_file:
                for line in data:
                    write_file.write(self.decode(line))
                    write_file.flush()

def main():
    df = pd.read_csv('~/.c/cyphers.csv')

    test_cypher = Cypher(list(df['key'])[0], list(df['alphabet'])[0])

    print(test_cypher.encode("This is a test.  Does the cypher's encoding work properly?"), "encoding test")
    print(test_cypher.decode(test_cypher.encode("This is a test.  Does the cypher's decoding work properly?")), "decoding test")

    test_cypher.encode_file('../../../.c/users-encoded.csv', '../../../.c/users.csv')
    test_cypher.decode_file('../../../.c/users.csv')

if __name__ == "__main__":
    main()