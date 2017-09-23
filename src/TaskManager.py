import glob, os

from FileHandler import FileHandler

class TaskManager(object):
    def __init__(self, Journal):
        self.journal = Journal
        print("==================================================")
        print(" Welcome. ")
        print("==================================================")
        self.menu()

    def menu(self):
        while True:
            print("================== Menu ======================")
            print(" 1 ) Store raw entries ")
            print(" 2 ) Get old entries ")
            print(" 3 ) Quit ")
            self.perform_task(input(" What would you like to do? "))

    def perform_task(self, task):
        switch = {
            '1' : self.store_raw_entries,
            '3' : self.journal.close
        }

        function = switch.get(task, self.print_error)

        return function()

    def store_raw_entries(self):
        os.chdir("../raw_entries")

        for entry in glob.glob("*.txt"):
            data = FileHandler().get_file_data(file_location=entry)
            FileHandler().save_and_encode(file_location=entry, journal=self.journal, data=data)

    def print_error(self):
        print('invalid input')