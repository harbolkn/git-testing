import csv

def read_csv(filepath):
    """
    Read data from a CSV file.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        list: A list containing the data from the CSV file.
    """
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

def write_csv(filepath, data):
    """
    Write data to a CSV file.

    Args:
        filepath (str): The path to the CSV file.
        data (list): The data to be written to the CSV file.

    Returns:
        None
    """
    with open(filepath, mode='w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        # Write the header row with field names
        writer.writeheader()

        # Write data rows
        for row in data:
            writer.writerow(row)
