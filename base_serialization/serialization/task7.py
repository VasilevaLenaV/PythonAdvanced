import csv
import pickle
import os


# 0. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.


def read_csv(filename):
    rows = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for r in str(row).split('\t'):
                rows.append(row)
    return rows


def read_csv_dr(filename):
    rows = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)
    return rows


def csv_to_pickle(data):
    return pickle.dumps(data)


def csv_to_pickle_file(file):
    result = read_csv(file)
    filename = os.path.splitext(file)[0]
    with open(f'{filename}.pickle', 'wb') as dump_out:
        pickle.dump(result, dump_out)


def csv_to_dict(filename):
    with open(filename, mode='r') as infile:
        reader = csv.DictReader(infile, skipinitialspace=True)
        return [r for r in reader]


def dict_to_pickle_file(dict,name):
    with open(f'{name}.pickle', 'wb') as dump_out:
        pickle.dump(dict, dump_out)



