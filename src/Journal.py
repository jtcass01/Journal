from Cypher import Cypher
import pandas as pd
import time
import os

current_directory = '/home/durzo/PycharmProjects/Journal/'

class Journal(object):
    def __init__(self, config_folder):
        self.cypher = self.build_cypher()
        self.decode_config_files(config_folder)
        self.username, self.password = self.prove_credentials()
        self.menu()
        self.close()

    def decode_config_files(self, config_folder):
        if not os.path.exists(current_directory + 'tmp/'):
            os.makedirs(current_directory + 'tmp/')

        time.sleep(3)

        self.cypher.decode_file(config_folder+'users.csv', file_destination= current_directory + 'tmp/users.csv')

    def remove_config_files(self):
        os.remove(current_directory + 'tmp/users.csv')
        os.rmdir(current_directory + 'tmp/')

    def build_cypher(self):
        cypher_DataFrame = pd.read_csv('~/.c/cyphers.csv')

        cypher = Cypher(list(cypher_DataFrame['key'])[0],list(cypher_DataFrame['alphabet'])[0])

        return cypher

    def prove_credentials(self):
        user_DataFrame = pd.read_csv(current_directory + 'tmp/users.csv')

        while True:
            username = input("username: ")
            password = input("password: ")

            for DataFrame_index in range(0, len(user_DataFrame)):
                if username == list(user_DataFrame['username'])[DataFrame_index] and password == list(user_DataFrame['password'])[DataFrame_index]:
                    return username, password
            else:
                print("Username and password not found.")


    def menu(self):
        print("==================================================")
        print(" Welcome. ")
        print("==================================================")

        while True:
            print("================== Menu ======================")
            print(" 1 ) Store raw entries ")
            print(" 2 ) Get old entries ")
            print(" 3 ) Quit ")
            input(" What would you like to do? ")

    def close(self):
        self.remove_config_files()

def main():
    test_journal = Journal('../../../.c/')

if __name__ == "__main__":
    main()