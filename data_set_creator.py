import random

data_list = list()
for i in range(100):
    i = random.randint(0, 100)
    data_list.append(i)

bdata = open("big_data.txt", "w")

for line in data_list:
    bdata.write(str(line) + "\n")

bdata.close()

# Code is creating one extra line at the end.
# It does not matter because it will not added to sql database.
# Main code does not allow that.
