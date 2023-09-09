import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

return read_csv('input.csv')