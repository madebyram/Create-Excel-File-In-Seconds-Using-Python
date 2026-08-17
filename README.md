# Create-Excel-File-In-Seconds-Using-Python

## How it Works

This script automates the conversion of raw, space-separated text data (`tfile.txt`) into a structured CSV format (`file.csv`). It starts by importing Python's built-in `csv` module and opening both the source text file for reading and the destination CSV file for writing. Using a `for` loop, the program reads the text file line-by-line and uses the `.split(" ")` function to divide each line into a list of individual words. Assuming each line follows a specific pattern (Serial Number, First Name, Last Name, Phone Number), the script intelligently concatenates the first and last name into a single "Full Name" string. Finally, it groups the serial number, full name, and phone number into a clean list and writes it as a new row into the CSV file using `writerow()`, before safely closing the file to save the data.
