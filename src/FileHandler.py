import os

class FileHandler(object):
    def __init__(self, log_folder = "log", raw_entry_folder = "raw_entries"):
        self.log_folder = log_folder
        self.raw_entry_folder = raw_entry_folder

    def save_and_encode(self, journal = None, file_location = None, data = None):
        os.chdir("../" + self.log_folder)
        date_path = self.get_date_path(file_location)

        self.define_path(date_path)

        with open(date_path, "w") as output_file:
            output_file.write(journal.cypher.encode(data))

        os.chdir("../" + self.raw_entry_folder)
        os.remove(file_location)

    def get_file_data(self, file_location = None):
        os.chdir("../" + self.raw_entry_folder)

        with open(file_location, "r") as file:
            return file.read()

    def define_path(self,  file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def get_date_path(self, file_name):
        date = file_name[:-4]
        month, day, year = date.split("-")
        return year + "/" + self.month_num_to_word(month) + "/" + file_name

    def month_num_to_word(self, month_number):
        month_number = str(month_number)

        switch = {
            '1' : 'January',
            '2' : 'February',
            '3' : 'March',
            '4' : 'April',
            '5' : 'May',
            '6' : 'June',
            '7' : 'July',
            '8' : 'August',
            '9' : 'September',
            '10': 'October',
            '11': 'November',
            '12': 'December',
        }

        month_word = switch.get(month_number)

        return month_word


def main():
    print(FileHandler().get_date_path(file_name="9-23-2017.txt"))

if __name__ == "__main__":
    main()