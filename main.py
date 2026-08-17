"""
    @Program: CSV file data adding
"""

# Importing Module
import csv

# opening files
file = open("file.csv", "w+", newline = "")
tf = open ("tfile.txt", "r") # Data

# Creating Writer
w = csv.writer(file)

# Cursor position to starting
tf.seek(0)

# Using for loop for adding Data
for line in tf:
    i = line.split(" ")
    # u may change it according to you
    sr = i[0]
    name = i[1] + " " + i[2]
    phone = i[3].strip()
    data = [sr, name, phone]
    # adding data
    w.writerow(data)
    file.flush()

# Closing Number
file.close()