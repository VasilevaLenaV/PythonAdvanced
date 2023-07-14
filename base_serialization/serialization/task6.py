import pickle
import csv


def pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file, 'rb') as f:
        data = pickle.load(f)

    headers = data[0].keys()

    with open(csv_file, 'w', newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
