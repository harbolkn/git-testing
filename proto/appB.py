import csv
import argparse

def read_csv(filepath):
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="CSV file to read")
    args = parser.parse_args()

    result = read_csv(args.filename)
    print(result)