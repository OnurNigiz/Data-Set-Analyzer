import create_sqldatabase
import sqlite3


# Create a sqlite data base.
MyDatabase = create_sqldatabase.Data_Set()
MyDatabase.create_dataset()

data = sqlite3.connect('database.sqlite')
dataCur = data.cursor()


# How many data are there?
dataCur.execute('SELECT COUNT(*) FROM Numbers')
row_number = dataCur.fetchone()  # Tuple include 1 item, it's the answer
row = row_number[0]

SIZE = 0
SUM = 0
MIN = None
MAX = None
for i in dataCur.execute('SELECT number, repetitions FROM Numbers'):
    SIZE = SIZE + i[1]
    SUM = SUM + i[0]*i[1]
    if MIN == None or MIN > i[0]:
        MIN = i[0]
    if MAX == None or MAX < i[0]:
        MAX = i[0]



print(f'There are {SIZE} valid numbers in database.')
print(f'Sum of all datas: {SUM}')
print("Max. number: ", MAX)
print("Min. number: ", MIN)

# Arithmetic mean value of data set
ar_mean = SUM / SIZE
print("Arithmetic mean: ", round(ar_mean, 2))
