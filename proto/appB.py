import csv
import sys

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

if len(sys.argv) > 1:
    filename = sys.argv[1]
    result = read_csv(filename)
    print(result)
else:
    print("Please provide a filename as a system argument.")