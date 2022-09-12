import sqlite3


class Data_Set():

    def __init__(self):

        # Read data from existing txt file
        self.fname = input("Enter file: ")
        if len(self.fname) < 1:
            self.fname = "big_data.txt"
        self.fh = open(self.fname)
        self.NoA = 0
        self.valid = 0
        self.numbers_list = list()
        self.listTup = list()

    def create_dataset(self):

        # Number of data / STORAGE for dataset
        # Written for cases with one integer data per row

        for line in self.fh:
            self.valid += 1
            if type(line) != int:
                try:
                    line = int(line)
                    self.NoA += 1
                    self.numbers_list.append(line)
                except:
                    print(f"Invalid data type, line {self.valid}")
                    continue
            else:
                self.NoA += 1
                self.numbers_list.append(line)

        for i in self.numbers_list:
            a = self.numbers_list.count(i)
            if (i, a) not in self.listTup:
                self.listTup.append((i, a))

        # Create a database
        self.conn = sqlite3.connect('database.sqlite')
        self.cur = self.conn.cursor()
        self.cur.execute('DROP TABLE IF EXISTS Numbers')
        self.cur.execute(
            '''CREATE TABLE Numbers (number INTEGER, repetitions INTEGER)''')

        # Insert data to sql database
        for i in range(len(self.listTup)):
            self.cur.execute('''INSERT INTO Numbers (number, repetitions) VALUES (?, ?)''',
                             (int(self.listTup[i][0]), int(self.listTup[i][1])))

            # Update sqlite folder every ... data input
            # For 1M data, it takes about 5 secs in CPU (related to mode part)
            if ((i+1) % 1) == 0:
                self.conn.commit()

        print(f"""{self.NoA-self.valid} invalid data detected.\n{self.NoA} valid data were collected from '{self.fname}'.""")
        self.conn.close()
