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
    with open(filepath, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)