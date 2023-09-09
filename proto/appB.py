import csv

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def write_csv(filepath, data):
    with open(filepath, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row with field names
        writer.writeheader()

        # Write data rows
        for row in data:
            writer.writerow(row)